from fastapi import Request, HTTPException

from fast.web import main


# Handlers
async def not_found_error(
    request: Request, 
    exc: HTTPException
):
    return main.templates.TemplateResponse(
        'pages/404.html', { 'request': request }, status_code=404
    )

async def internal_error(
    request: Request, 
    exc: HTTPException
):
    return main.templates.TemplateResponse(
        'pages/500.html', { 'request': request }, status_code=500
    )


exception_handlers = {
    404: not_found_error,
    500: internal_error
}
