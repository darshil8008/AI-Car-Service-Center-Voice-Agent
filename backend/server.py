# import os
# from livekit import api
# from flask import Flask, request
# from dotenv import load_dotenv
# from flask_cors import CORS
# from livekit.api import LiveKitAPI, ListRoomsRequest
# import uuid

# load_dotenv()

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# async def generate_room_name():
#     name = "room-" + str(uuid.uuid4())[:8]
#     rooms = await get_rooms()
#     while name in rooms:
#         name = "room-" + str(uuid.uuid4())[:8]
#     return name

# async def get_rooms():
#     api = LiveKitAPI()
#     rooms = await api.room.list_rooms(ListRoomsRequest())
#     await api.aclose()
#     return [room.name for room in rooms.rooms]

# @app.route("/getToken")
# async def get_token():
#     name = request.args.get("name", "my name")
#     room = request.args.get("room", None)
    
#     if not room:
#         room = await generate_room_name()
        
#     token = api.AccessToken(os.getenv("LIVEKIT_API_KEY"), os.getenv("LIVEKIT_API_SECRET")) \
#         .with_identity(name)\
#         .with_name(name)\
#         .with_grants(api.VideoGrants(
#             room_join=True,
#             room=room
#         ))
    
#     return token.to_jwt()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001, debug=True)




# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from dotenv import load_dotenv
# import os
# import uuid
# from livekit.api.access_token import AccessToken, VideoGrants

# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# @app.route("/getToken")
# def get_token():
#     name = request.args.get("name", "guest")
#     room = request.args.get("room", f"room-{uuid.uuid4().hex[:8]}")

#     token = (
#         AccessToken()
#         .with_identity(name)
#         .with_name(name)
#         .with_grants(VideoGrants(room_join=True, room=room))
#     )

#     return jsonify({
#         "token": token.to_jwt(),
#         "url": os.getenv("LIVEKIT_WS_URL"),
#         "room": room
#     })

# if __name__ == "__main__":
#     app.run(port=5001, debug=True)


# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from livekit.api import LiveKitAPI, ListRoomsRequest
# from livekit.api.access_token import AccessToken, VideoGrants
# import uuid
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# async def get_rooms():
#     api = LiveKitAPI()
#     rooms = await api.room.list_rooms(ListRoomsRequest())
#     await api.aclose()
#     return [room.name for room in rooms.rooms]

# async def generate_room_name():
#     name = "room-" + str(uuid.uuid4())[:8]
#     rooms = await get_rooms()
#     while name in rooms:
#         name = "room-" + str(uuid.uuid4())[:8]
#     return name

# @app.get("/getToken")
# async def get_token(name: str = "guest", room: str | None = None):
#     room = room or await generate_room_name()

#     token = AccessToken(
#         api_key=os.getenv("LIVEKIT_API_KEY"),
#         api_secret=os.getenv("LIVEKIT_API_SECRET"),
#         identity=name
#     )
#     token.add_grant(VideoGrants(room_join=True, room=room))

#     return {
#         "token": token.to_jwt(),
#         "url": os.getenv("LIVEKIT_WS_URL"),
#         "room": room
#     }

# @app.get("/")
# async def root():
#     return {"status": "LiveKit FastAPI server running."}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("server:app", host="0.0.0.0", port=5001, reload=True)


# backend/server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from livekit.api.access_token import AccessToken, VideoGrants
import os
import uuid

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getToken")
def get_token(name: str = "Darshil", room: str = ""):
    if not room:
        room = "room-" + str(uuid.uuid4())[:8]

    token = AccessToken(
        os.getenv("LIVEKIT_API_KEY"),
        os.getenv("LIVEKIT_API_SECRET")
    ).with_identity(name).with_name(name).with_grants(
        VideoGrants(room_join=True, room=room)
    )

    return {"token": token.to_jwt(), "room": room}
