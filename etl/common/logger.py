from rich.console import Console
console = Console()

def success_log(text):
  console.print(text, style="bold green")

def warning_log(text):
  console.print(text, style="bold yellow")

def error_log(text):
  console.print(text,style="bold red")