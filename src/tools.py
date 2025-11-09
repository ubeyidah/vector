import subprocess
from google.genai import types

ALLOWED_APPS = ["alacritty", "btop", "nvim", "yazi", "nautilus"]


def _run_safe_hyprctl(command_list: list):
    """Run hyprctl command safely."""
    try:
        full_command = ["hyprctl", "-j"] + command_list
        result = subprocess.run(
            full_command,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8",
        )
        print(f"[Tool Executed: hyprctl -j {' '.join(command_list)}]")
        return {"status": "success", "output": result.stdout}
    except Exception as e:
        print(f"[Tool Error: {str(e)}]")
        return {"status": "error", "message": str(e)}


def tool_open_applications(app_name: str):
    """Open specified application if it is allowed."""
    app_name_lower = app_name.lower()
    if app_name_lower in ALLOWED_APPS:
        return _run_safe_hyprctl(["dispatch", "exec", app_name_lower])
    else:
        print(f"[Tool Error: App '{app_name}' is not on allow-list]")
        return {
            "status": "error",
            "message": f"Application '{app_name}' is not allowed.",
        }


all_tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="tool_open_applications",
                description=f"Opens an application on the user's computer, e.g. {', '.join(ALLOWED_APPS)}.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "app_name": types.Schema(
                            type=types.Type.STRING,
                            description=f"The name of the app to open, e.g. {', '.join(ALLOWED_APPS)}",
                        )
                    },
                    required=["app_name"],
                ),
            )
        ]
    )
]
