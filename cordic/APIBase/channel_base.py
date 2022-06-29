import cordic
from cordic.models.channel import Channel
from typing import Union


async def fetch_channel_base(channel_id: int) -> Channel:

    """Gets a channel by id"""

    client = cordic.CurrentClient.get_client()

    rs = await client.http.request("GET", f"/channels/{channel_id}")
    return Channel(await rs.json())