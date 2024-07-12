import asyncio
import aiofiles
import argparse
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor as executor


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


async def list_files(source_folder: Path):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: list(source_folder.glob('**/*')))


async def read_folder(source_folder: Path, output_folder: Path):
    files = await list_files(source_folder)
    tasks = []
    for file_path in files:
        if file_path.is_file():
            tasks.append(copy_file(file_path, output_folder))
    await asyncio.gather(*tasks)


async def copy_file(file_path: Path, output_folder: Path):
    try:
        ext = file_path.suffix.lstrip(".").lower()
        target_folder = output_folder / ext
        target_folder.mkdir(parents=True, exist_ok=True)
        target_path = target_folder / file_path.name
        async with aiofiles.open(file_path, "rb") as f_src:
            async with aiofiles.open(target_path, "wb") as f_dst:
                while chunk := await f_src.read(1024):
                    await f_dst.write(chunk)
        logging.info(f"File {file_path} was copied {target_path}")
    except Exception as e:
        logging.error(f"Exception happens during file {file_path} copy: {e}")


async def main(source_folder: Path, output_folder: Path):
    await read_folder(source_folder, output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File sorting by extension.")
    parser.add_argument("--source", type=Path, help="Source folder")
    parser.add_argument("--dest", type=Path, help="Destination folder")
    args = parser.parse_args()
    source_folder = args.source
    output_folder = args.dest
    asyncio.run(main(source_folder, output_folder))
