from fastapi import FastAPI, Form, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from fastapi.responses import JSONResponse

app = FastAPI()

MONGO_URI = "mongodb+srv://debruyns:DAMLore@damlore-cluster.qn1o6.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["debruyns"]
collection = db["landmarks"]
tours = db["tours"]

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/map")
async def get_map(request: Request, tag: str = Query("", alias="tag")):
    # Fetch all distinct tags from the collection
    available_tags = sorted(set(collection.distinct("tag")))

    # Filter landmarks by the selected tag
    if tag:
        landmarks = list(collection.find({"tag": tag}, {"_id": 0, "name": 1, "location": 1, "description": 1, "tag": 1}))
    else:
        landmarks = list(collection.find({}, {"_id": 0, "name": 1, "location": 1, "description": 1, "tag": 1}))

    # Format landmarks as markers
    markers = []
    for landmark in landmarks:
        location = landmark["location"].split(",")
        if len(location) == 2:
            lat, lng = float(location[0]), float(location[1])
            markers.append({
                "lat": lat,
                "lng": lng,
                "name": f"<b>{landmark['name']}</b>",
                "description": f"<br>{landmark['description']}",
                "tag": landmark['tag']  # Include the tag for filtering on the frontend
            })

    # Pass markers and other necessary information to the template
    return templates.TemplateResponse("map.html", {
        "request": request,
        "markers": markers,
        "available_tags": available_tags,
        "selected_tag": tag,
    })


@app.get("/about")
async def get_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/mission")
async def get_mission(request: Request):
    return templates.TemplateResponse("mission.html", {"request": request})

@app.get("/lore")
async def get_lore(request: Request, tag: str = Query("", alias="tag")):
    available_tags = sorted(set(collection.distinct("tag")))
    if tag:
        landmarks = list(collection.find({"tag": tag}, {"_id": 0}))
    else:
        landmarks = list(collection.find({}, {"_id": 0}))
    return templates.TemplateResponse("lore.html", {"request": request, "landmarks": landmarks, "available_tags": available_tags, "selected_tag": tag})

@app.get("/tour/{tour_name}")
async def get_tour(request: Request, tour_name: str):
    tour = tours.find_one({"name": tour_name}, {"_id":0})
    if not tour:
        return JSONResponse(status_code=404, content={"message": "Tour not found"})
    return templates.TemplateResponse("tour.html", {"request": request, "tour": tour})

@app.get("/adder")
async def get_adder(request: Request):
    return templates.TemplateResponse("adder.html", {"request": request})

@app.post("/adder")
async def post_adder(
    name: str = Form(...),
    image_url: str = Form(...),
    description: str = Form(...),
    location: str = Form(...),
    location_name: str = Form(...),
    id_tag: str = Form(None),
):
    new_landmark = {
        "name": name,
        "image_url": image_url,
        "description": description,
        "location": location,
        "location_name": location_name,
        "tag": id_tag
    }
    collection.insert_one(new_landmark)
    return {"message": "Landmark added successfully!"}

@app.get("/itinerary")
async def get_itinerary(request:Request):
    avail_tours = list(tours.find({}, {"_id":0, "name":1, "description":1}))
    return templates.TemplateResponse("itinerary.html", {"request":request, "tours":avail_tours})

@app.get("/engagement")
async def get_engagement(request:Request):
    return templates.TemplateResponse("engagement.html", {"request": request})