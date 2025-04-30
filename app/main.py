from .utils import common_class
from .services_processed import zalora_bl, lazada_bl
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware


def combine_queries(query, sort, sortdir):
    z_temp = zalora_bl.GET_zaloraproductlist(query, sort, sortdir)
    l_temp = lazada_bl.GET_lazadaproductlist(query, sort)

    all_items = z_temp.items + l_temp.items

    return common_class.DataResponse (
        items = all_items
    )


app = FastAPI()

resp_model = common_class.DataResponse


origins = [
    "http://localhost:3000",  # React frontend URL
    "http://127.0.0.1:3000",  # If you want to allow the backend URL too
    "*",  # Allow all origins (use with caution in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/zalora/data", response_model=resp_model)
async def get_data(
        query: str = Query(..., description="Search term"),
        sort: str = Query("popularity", description="Sort method"),
        sort_dir: str = Query("desc", description="Sort direction"),
    ):
    return combine_queries(query, sort, sort_dir)




