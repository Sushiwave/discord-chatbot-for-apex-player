from ....globalvalue import globalvalue as v





async def send(ctx, message):
    if ctx.message.channel.id == v.channel_id:
        await ctx.send(message)

async def send_message_list(ctx, message_list):
    for message in message_list:
        await send(ctx, message)

