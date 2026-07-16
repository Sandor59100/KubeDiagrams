"""Service Data Model"""
from typing import Optional

class DiagramResult:
    """Data model for the diagram result."""
    def __init__(
        self,
        success: bool,
        diagram: Optional[str] = None,
        mime_type: Optional[str] = None,
        filename: Optional[str] = None,
        message: Optional[str] = None,
        error: Optional[str] = None,
        command: Optional[str] = None,
        stdout: Optional[str] = None,
        stderr: Optional[str] = None
    ):
        self.success = success
        self.diagram = diagram
        self.mime_type = mime_type
        self.filename = filename
        self.message = message
        self.error = error
        self.command = command
        self.stdout = stdout
        self.stderr = stderr

    def to_dict(self) -> dict:
        """Converts the DiagramResult to a dictionary."""
        result = {}
        if self.success:
            result.update({
                "diagram": self.diagram,
                "mimeType": self.mime_type,
                "filename": self.filename,
                "message": self.message,
                "command": self.command,
                "stdout": self.stdout or "",
                "stderr": self.stderr or "",
            })
        else:
            result["error"] = self.error
        return result
