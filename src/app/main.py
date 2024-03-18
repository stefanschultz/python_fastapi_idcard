# main.py

from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List

from models import IDCard
from example_data import id_cards_examples

app = FastAPI()

id_cards = {key: value for (key, value) in id_cards_examples.items()}


@app.post("/id-cards/", response_model=IDCard)
def create_id_card(id_card: IDCard):
    """Create a new IDCard."""
    id_cards[id_card.id] = id_card
    return id_card


@app.get("/id-cards/{id_card_id}", response_model=IDCard)
def get_id_card(id_card_id: UUID):
    """Get an IDCard by its ID."""
    if id_card_id not in id_cards:
        raise HTTPException(status_code=404, detail="IDCard not found")
    return id_cards[id_card_id]


@app.get("/id-cards/", response_model=List[IDCard])
def get_id_cards():
    """Get all IDCards."""
    return list(id_cards.values())


@app.put("/id-cards/{id_card_id}", response_model=IDCard)
def update_id_card(id_card_id: UUID, id_card: IDCard):
    """Update an IDCard by its ID."""
    if id_card_id not in id_cards:
        raise HTTPException(status_code=404, detail="IDCard not found")
    id_cards[id_card_id] = id_card
    return id_card


@app.delete("/id-cards/{id_card_id}", response_model=IDCard)
def delete_id_card(id_card_id: UUID):
    """Delete an IDCard by its ID."""
    if id_card_id not in id_cards:
        raise HTTPException(status_code=404, detail="IDCard not found")
    return id_cards.pop(id_card_id)