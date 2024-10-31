from fastapi import HTTPException
from fastapi import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse
from src.services import link_service
from src.models import dto    


router = APIRouter(prefix='/s')


@router.post('/shorten')
async def shorten(link: dto.Link):
    
    short_link = link_service.get_short(link.link)
    
    if not short_link:
        short_link = link_service.create(link.link)
        return JSONResponse(content={'data': short_link}, status_code=201)
    
    return JSONResponse(content={'data': short_link}, status_code=200)


@router.get('/{short_link}')
async def redirect(short_link: str):
    
    """Redirect user to needed link"""

    link = link_service.get_full(short_link=short_link)

    if not link:

        raise HTTPException(status_code=404, detail="Link not found")

    return RedirectResponse(link, status_code=301)


@router.delete('/delete', status_code=204)
async def delete(short_link: dto.Link):
    return link_service.delete(short_link)