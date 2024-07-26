import rich
from rich.console import Console
from os import path
import shlex
import pyuac

from utils.clitext import CLIText
from utils.helpers import preprocess_input, scan_dir, table_data, clean_temp_files

console = Console()

if __name__ == "__main__":
    while True:
        console.clear()
        if not pyuac.isUserAdmin():
            console.print(
                "[bold red]Without Administrative Privileges, The Program Might bypass certain files during scanning or deletion processes due to insufficient permissions granted by Windows.[/bold red]\n")

        for key, value in CLIText.commands.items():
            console.print(f"{key}: {value}")

        command_written = console.input("\n[bold yellow]$[/bold yellow]> ", markup=True)
        if command_written.strip() == "":
            continue

        if len(command_written.split(' ')) > 0 and command_written.split(' ') != int:
            parsed_command = shlex.split(preprocess_input(command_written), posix=False)

        command = int(parsed_command[0])
        argument = ""

        try:
            if command_written.split(' ')[1] != int:
                argument = ' '.join(parsed_command[1:])
                if argument.endswith('\\'):
                    argument = argument[:-1]

                argument = argument.replace('"', '')
        except:
            pass

        if command == 0:
            if int(argument) == 1:
                console.print(CLIText.INFO_1)
            elif int(argument) == 2:
                console.print(CLIText.INFO_2)
            else:
                console.print(
                    f"[yellow]#[/yellow]> [red]{argument} Doesn't Have Detailed Information Or Argument is Invalid.[/red]")

        elif command == 1:
            if argument == "." or argument == "":
                scan_dir(argument)
            elif not path.exists(argument):
                console.print("[yellow]#[/yellow]> [red]Path Not Found![/red]")

        elif command == 2:
            table_data(argument)
            pass

        elif command == 3:
            clean_temp_files()

        elif command == 4:
            console.clear()
            raise SystemExit()
        else:
            continue

        console.input("\n[bright_white][Enter][/bright_white] [bold orange3]To Continue[/bold orange3]")