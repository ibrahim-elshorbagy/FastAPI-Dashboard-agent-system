from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Init
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Routes
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "pages/home.html",
        {"request": request, "title": "Dashboard", "active_menu": "dashboard"}
    )

# ==================== Email Management Routes ====================
@router.get("/emails/inbox", response_class=HTMLResponse)
async def inbox(request: Request):
    return templates.TemplateResponse(
        "pages/Emails/inbox/inbox.html",
        {"request": request, "title": "Inbox", "active_menu": "emails", "active_submenu": "inbox"}
    )

@router.get("/emails/sent", response_class=HTMLResponse)
async def sent(request: Request):
    return templates.TemplateResponse(
        "pages/Emails/sent/sent.html",
        {"request": request, "title": "Sent Emails", "active_menu": "emails", "active_submenu": "sent"}
    )

@router.get("/emails/draft", response_class=HTMLResponse)
async def draft(request: Request):
    return templates.TemplateResponse(
        "pages/Emails/draft/draft.html",
        {"request": request, "title": "Draft Emails", "active_menu": "emails", "active_submenu": "draft"}
    )

@router.get("/emails/spam", response_class=HTMLResponse)
async def spam(request: Request):
    return templates.TemplateResponse(
        "pages/Emails/spam/spam.html",
        {"request": request, "title": "Spam", "active_menu": "emails", "active_submenu": "spam"}
    )

@router.get("/emails/bin", response_class=HTMLResponse)
async def bin(request: Request):
    return templates.TemplateResponse(
        "pages/Emails/bin/bin.html",
        {"request": request, "title": "Bin", "active_menu": "emails", "active_submenu": "bin"}
    )

# ==================== HR Management Route ====================
@router.get("/hr", response_class=HTMLResponse)
async def hr(request: Request):
    return templates.TemplateResponse(
        "pages/Hr/index.html",
        {"request": request, "title": "HR Management", "active_menu": "hr"}
    )

# ==================== Reports Management Route ====================
@router.get("/reports", response_class=HTMLResponse)
async def reports(request: Request):
    return templates.TemplateResponse(
        "pages/Reports/index.html",
        {"request": request, "title": "Reports", "active_menu": "reports"}
    )

# ==================== Settings Route ====================
@router.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse(
        "pages/settings.html",
        {"request": request, "title": "Settings", "active_menu": "settings"}
    )
