# main.py

from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
import os
from dotenv import load_dotenv
import redis

from models import IDCard
from example_data import id_cards_examples

load_dotenv()  # take environment variables from .env.

STORAGE_TYPE = os.getenv("STORAGE_TYPE", "in-memory")  # Define the storage type.

app = FastAPI()  # create a FastAPI instance.

# internal storage as fallback if no external storage is used.
id_cards = {}

# Redis storage, if used.
if STORAGE_TYPE == "redis":
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def save_id_card(card_id: str, id_card: IDCard) -> IDCard:
    """Save an IDCard by its ID."""
    if STORAGE_TYPE == "redis":
        for key, value in id_card.convert_to_json_object().items():
            r.hset(card_id, key, value)
    else:
        id_cards[id] = id_card.dict()
    return id_card


def get_id_card(card_id: str):
    """Get an IDCard by its ID."""
    if STORAGE_TYPE == "redis":
        return r.hgetall(card_id)
    return id_cards.get(card_id, None)


@app.post("/id-cards/", response_model=IDCard)
def create_id_card(id_card: IDCard):
    """Create a new IDCard."""
    card_id = str(id_card.id)
    save_id_card(card_id, id_card)
    id_cards[id_card.id] = id_card
    return {"id": card_id, **id_card.dict()}


@app.get("/id-cards/{card_id}", response_model=IDCard)
def get_id_card(card_id: str):
    """Get an IDCard by its ID."""
    id_card_data = get_id_card(card_id)
    if id_card_data:
        return {"id": card_id, **id_card_data}
    raise HTTPException(status_code=404, detail="ID card not found")


@app.get("/id-cards/", response_model=List[IDCard])
def get_id_cards():
    """Get all IDCards."""
    if STORAGE_TYPE == "redis":
        keys = r.keys()
        return [r.hgetall(key) for key in keys]
    return list(id_cards.values())


@app.put("/id-cards/{card_id}", response_model=IDCard)
def update_id_card(card_id: UUID, id_card: IDCard):
    """Update an IDCard by its ID."""
    if card_id not in id_cards:
        raise HTTPException(status_code=404, detail="ID card not found")
    id_cards[card_id] = id_card
    return id_card


@app.delete("/id-cards/{card_id}", response_model=IDCard)
def delete_id_card(card_id: str):
    """Delete an IDCard by its ID."""
    if STORAGE_TYPE == "redis":
        if r.exists(card_id):
            r.delete(card_id)
            return {"status": "ok", "message": "ID card deleted"}
        else :
            raise HTTPException(status_code=404, detail="ID card not found")
    else:
        if card_id in id_cards:
            del id_cards[card_id]
            return {"status": "ok", "message": "ID card deleted"}
        else:
            raise HTTPException(status_code=404, detail="ID card not found")


@app.delete("/clear-data/")
def clear_data():
    """Clear all data."""
    if STORAGE_TYPE == "redis":
        r.flushdb()
    else:
        id_cards.clear()
    return {"status": "ok", "message": "All data cleared."}


@app.get("/storage-type/")
def get_storage_type():
    """Get the storage type."""
    return {"storage_type": STORAGE_TYPE}


@app.get("/health/")
def health():
    """Health check."""
    return {"status": "ok", "message": "Service is healthy."}


@app.get("/get-id-card-example/")
def get_example() -> dict:
    """Get example data."""
    return id_cards_examples


@app.get("/write-id-card-example/")
def write_id_card_example() -> dict:
    """Write example data to the storage."""
    print("Examples:", id_cards_examples)
    for card_id, id_card in id_cards_examples.items():
        save_id_card(card_id, id_card)
    return {
        "status": "ok",
        "message": "Example data written to the storage.",
        "id_cards": id_cards_examples
    }