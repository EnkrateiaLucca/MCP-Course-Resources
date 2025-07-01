"""
Personal Assistant MCP Server

A minimal MCP server that acts as a personal assistant for file management,
git operations, and email notifications. Perfect for intro MCP courses.
"""

import os
import base64
from pathlib import Path
from typing import Dict, List
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv() 

mcp = FastMCP("simple_mcp")


@mcp.tool()
def create_file(file_path: str, content: str) -> Dict[str, str]:
    """
    Create a new file with the specified content.
    
    Args:
        file_path: Path where the file should be created
        content: Content to write to the file
        
    Returns:
        Dictionary with success/error status
    """
    try:
        path = Path(file_path)
        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {"success": True, "message": f"File created successfully: {file_path}"}
    except Exception as e:
        return {"success": False, "error": f"Failed to create file: {str(e)}"}

@mcp.tool()
def read_file(file_path: str) -> Dict[str, str]:
    """
    Read the contents of a file.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        Dictionary containing file contents or error
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return {"success": False, "error": f"File not found: {file_path}"}
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {"success": True, "content": content, "file_path": file_path}
    except Exception as e:
        return {"success": False, "error": f"Failed to read file: {str(e)}"}

@mcp.tool()
def update_file(file_path: str, content: str) -> Dict[str, str]:
    """
    Update an existing file with new content.
    
    Args:
        file_path: Path to the file to update
        content: New content for the file
        
    Returns:
        Dictionary with success/error status
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return {"success": False, "error": f"File not found: {file_path}"}
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {"success": True, "message": f"File updated successfully: {file_path}"}
    except Exception as e:
        return {"success": False, "error": f"Failed to update file: {str(e)}"}

@mcp.tool()
def list_files(directory_path: str) -> Dict[str, any]:
    """
    List all files and directories in the specified path.
    
    Args:
        directory_path: Path to the directory to list
        
    Returns:
        Dictionary containing files and directories or error
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            return {"success": False, "error": f"Directory not found: {directory_path}"}
        
        if not path.is_dir():
            return {"success": False, "error": f"Path is not a directory: {directory_path}"}
        
        files = []
        directories = []
        
        for item in path.iterdir():
            if item.is_file():
                files.append(item.name)
            elif item.is_dir():
                directories.append(item.name)
        
        return {
            "success": True,
            "path": directory_path,
            "files": sorted(files),
            "directories": sorted(directories)
        }
    except Exception as e:
        return {"success": False, "error": f"Failed to list directory: {str(e)}"}


if __name__=="__main__":
    # Running the server with streamable-http transport
    mcp.run(transport="streamable-http")