#!/usr/bin/env python3
"""
Save this file as 'create_guide.py' and run it.
The PDF will appear in the same folder.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable
)
from reportlab.lib.colors import HexColor
import os

# [PASTE THE ENTIRE SCRIPT FROM YOUR MESSAGE HERE]
# ... (all the code from your original message, but with the build() function modified as below)

def build():
    # FIXED: Use current directory instead of Linux path
    out = "DataQuest_Python_Collections_Guide.pdf"
    
    doc = SimpleDocTemplate(
        out, pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=25*mm, bottomMargin=20*mm,
        title="Data Quest: Mastering Python Collections",
        author="Complete Beginner's Guide",
    )
    
    S = make_styles()
    story = build_content(S)
    
    doc.build(story,
              onFirstPage=draw_cover,
              onLaterPages=draw_page)
    print(f"✅ PDF created: {os.path.abspath(out)}")

if __name__ == "__main__":
    build()