from dataclasses import dataclass

from utils.helpers import availible_drives

@dataclass
class CLIText:
    INFO_1 = '1: Scan Drives | arg = Path[Argument Can Also be Drives Themselvs eg. "C:/"][yellow](if "." is given as an argument it will scan all availible drives.)[/yellow] | example usage: 1 "C:/..."'
    INFO_2 = f'2: View Scanned Data | arg = Drive/CustomPathScanned{availible_drives()} ||| OPTIONAL(USE ONLY ONE) -> args[--max-line [LINE LIMIT], --size-threshold [100 KB, 1 MB, 10 GB, 1 TB] | Example Usage: 2 [green]C[/green] --max-line 100 OR --size-threshold 100 MB'

    commands = {
        "0": "Gives you Detailed Information About a Command | example usage: 0 1",
        "1": 'Scan Drives | arg = Path or Drive| example usage: 1 "C:/..." | More Information In 0',
        "2": f'View Scan Data | arg = {availible_drives()}/CustomPath | Example Usage: 2 [green]C[/green] --max-line 100 OR --size-threshold 100MB',
        "3": "Clean Temp Files",
        "4": "Exit"
    }