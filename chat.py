import asyncio

from sydney import SydneyClient


async def main() -> None:
    async with SydneyClient() as sydney:
        while True:
            prompt = input("You: ")

            if prompt == "!reset":
                await sydney.reset_conversation()
                continue
            elif prompt == "!exit":
                break

            print("Sydney: ", end="", flush=True)
            ans = await sydney.ask(prompt)
            print(ans)
            #async for response in sydney.ask_stream(prompt):
            #    print(response, end="", flush=True)
            print("\n")



asyncio.run(main())