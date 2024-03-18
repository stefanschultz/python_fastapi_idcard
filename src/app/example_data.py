# example_data.py

from uuid import uuid4
from models import IDCard

id_card_john_doe = IDCard(
        first_name="John",
        last_name="Doe",
        birth_date="1990-01-01",
        expiration_date="2030-01-01",
        is_active=True
    )
id_card_jane_doe = IDCard(
        first_name="Jane",
        last_name="Doe",
        birth_date="1995-01-01",
        expiration_date="2030-01-01",
        is_active=True
    )

id_cards_examples = {
    id_card_john_doe.id: id_card_john_doe,
    id_card_jane_doe.id: id_card_jane_doe
}