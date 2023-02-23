import unittest

import aiohttp as aiohttp


class TestEndpoints(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:5000"

    # fetch all users
    async def test_a(self) -> None:
        async with aiohttp.ClientSession() as client:
            async with client.get("http://127.0.0.1:5000/users") as r:
                self.assertTrue(r.status == 200)
                data: dict = await r.json()
                self.assertFalse(data["error"])  # assert that there are no errors
                self.assertIsInstance(data["users"], list)  # make sure the result is always a list

                x: dict
                for x in data['users']:
                    with self.subTest(x):  # result type checking if any is present
                        self.assertIsInstance(x, dict)
                        self.assertIn("name", x)
                        self.assertIn("age", x)

    # adds a user
    async def test_b(self, name: str = "deez", age: int = 69) -> None:
        async with aiohttp.ClientSession() as client:
            async with client.post(f"{self.base_url}/users/add", json={"name": name, "age": age}) as r:
                self.assertTrue(r.status == 200)
                self.assertFalse((await r.json())["error"])

    # tests fetching a user that we add
    async def test_c(self, name: str = "deez") -> int:
        async with aiohttp.ClientSession() as client:
            async with client.get(f"{self.base_url}/users/user", params={"name": name}) as r:  # query the given user, we assume it exists, run test_add_user to add a user
                self.assertTrue(r.status == 200)
                data: dict = await r.json()
                self.assertTrue(data["found"])
                self.assertIsInstance(data["user"], dict)

            async with client.get(f"{self.base_url}/users/user", params={"name": "non existant user"}) as r:  # try query a non existent user
                self.assertTrue(r.status == 200)
                data2: dict = await r.json()
                self.assertFalse(data2["found"])
                self.assertIsInstance(data2["user"], dict)

        return data["user"].get("id")

    # test updating the user
    async def test_d(self, user_id: int = 1, name: str = "new fancy name", age: int = 6969) -> None:
        async with aiohttp.ClientSession() as client:
            async with client.put(f"{self.base_url}/users/update", json={"id": user_id, "name": name, "age": age}) as r:
                self.assertTrue(r.status == 200)
                data: dict = await r.json()
                self.assertFalse(data["error"])
                self.assertTrue(data["success"])

    # deletes a user
    async def test_f(self, name: str = "new fancy name") -> None:
        async with aiohttp.ClientSession() as client:
            async with client.delete(f"{self.base_url}/users/delete/{name}") as r:
                self.assertTrue(r.status == 200)
                self.assertFalse((await r.json())["error"])

    # test all cases at once
    async def test_w_last_all(self):
        await self.test_a()  # fetch all suers
        await self.test_b(name="yes")  # add this user
        uid: int = await self.test_c(name="yes")  # query the same user
        await self.test_d(user_id=uid, name="new name", age=6969)  # update the user
        await self.test_f(name="new name")  # delete that user

        # assert that none of these 2 exist
        with self.assertRaises(AssertionError):
            await self.test_c(name="yes")  # should fail as the user should no longer exist
        with self.assertRaises(AssertionError):
            await self.test_c(name="new name")  # should fail as the user should no longer exist


if __name__ == '__main__':
    unittest.main()
