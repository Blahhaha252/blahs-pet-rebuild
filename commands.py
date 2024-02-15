from server_settings import serversettings, nullVar
async def sscommands(client, server, serverid, channelid, args, isowner):
    arg1 = args[0]
    arg2 = args[1] if len(args) > 1 else None
    arg3 = args[2] if len(args) > 2 else None
    print(arg1, arg2, arg3)
    arg1 = arg1[1:]
    watch_list_items = ['watched', 'watch_list']
    channel = client.get_channel(channelid)
    if arg1 in watch_list_items and arg2 is None and arg3 is None:
        watch_list = server.watched_list()
        await channel.send(watch_list)
    if arg1 in watch_list_items and arg2 == "add" and arg3 is None:
        await channel.send("You need to provide an role/userid to add")
    elif arg1 in watch_list_items and arg2 == "add" and arg3 is not None:
        server.watch_list_add(arg3)
        await channel.send(f"{arg3} saved to watch list")
    if arg1 in watch_list_items and arg2 == "remove" and arg3 is not None:
        try:
            server.watch_list_remove(arg3)
            await channel.send(f"{arg3} was removed")
        except nullVar as e:
            await channel.send(f"Raised exception: {e}")
    elif arg1 in watch_list_items and arg2 == "remove" and arg3 is None:
        await channel.send("You cant remove nothing, please provide a role/userid to remove")
#async def commands(server, serverid, channelid, args, isowner):
#    if isowner:
 #       await owner_commands(server, serverid, channelid, args)
 #   elif 
#async def owner_commands(server, serverid, channelid, args) 