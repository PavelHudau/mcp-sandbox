from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image

import pyautogui
import io


mcp = FastMCP("Screenshot MCP")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture a screenshot of the current screen.

    Returns:
        Image: The captured screenshot as an Image object.
    """
    try: 
        img_byte_arr = io.BytesIO()
        # if the file exceeds ~1MB, it will be rejected by Claude
        screenshot = pyautogui. screenshot()
        screenshot. convert("RGB"). save (img_byte_arr, format="JPEG", quality=60, optimize=True)
        return Image(data=img_byte_arr.getvalue(), format="jpeg")
    except Exception as e:
        print(f"An error occurred while capturing the screenshot: {str(e)}")
        raise


if __name__ == "__main__":
    mcp.run()
 