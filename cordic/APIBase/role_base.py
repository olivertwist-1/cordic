import cordic

from typing import List

from cordic.models.role import Role


async def fetch_roles_from_guild_base(guild_id: int) -> List[Role]:
    client = cordic.CurrentClient.get_client()

    rs = await client.http.request(
        "GET",
        f"/guilds/{guild_id}/roles"
    )
    return list(map(
        Role, await rs.json()
    ))