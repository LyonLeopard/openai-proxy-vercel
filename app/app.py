import aiohttp
from loguru import logger
from fastapi import FastAPI, Request, Response, HTTPException

app = FastAPI(debug=True)


@app.api_route("/{path:path}", methods=["GET", "POST", "DELETE", "PUT", "PATCH"])
async def proxy(request: Request, path):
    if not path.startswith("v"):
        return Response("Welcome to OpenAI Proxy")
    else:
        headers = dict(request.headers)
        auth_key = headers.get("authorization")
        if not auth_key:
            raise HTTPException(status_code=401, detail="Authorization key is required")
        target_url = f"https://api.openai.com/{path}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                        method=request.method,
                        url=target_url,
                        headers={
                            "Authorization": headers.get("authorization"),
                            "Content-Type": "application/json"
                        },
                        data=await request.body() if request.method != "GET" else None,
                ) as response:
                    response_content = await response.read()
                    log(response_content)
                    return Response(
                        content=response_content,
                        status_code=response.status,
                        headers=dict(response.headers)
                    )
            except Exception as e:
                logger.error(f"Error during forwarding request: {e.__str__()}")
                return Response("Internal server error", status_code=500)


def log(bytes_string: bytes) -> None:
    json_string = bytes_string.decode("utf-8")
    logger.info(json_string)
