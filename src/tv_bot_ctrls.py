#
# Excellent Regards, the Alveare Solutions #!/Society -x
#
# BOT CTRLS

import logging
import asyncio

log = logging.getLogger('TeleVision')

# TODO
async def start(update, context):
    '''
    [ NOTE ]: Function that will be called when the /start command is received
    '''
    log.debug('TODO - FIX ME')
    await update.message.reply_text('Welcome to TeleVision!')
async def help(update, context):
    '''
    [ NOTE ]: Function that will be called when the /help command is received
    '''
    log.debug('TODO - FIX ME')
    await update.message.reply_text(
        "Smile! You're on TeleVision!"
    )
async def error(update, context):
    '''
    [ NOTE ]: Log Errors caused by Updates.
    '''
    log.warning(
        'Update ({}) caused error ({})'.format(update, context.error)
    )
async def echo(update, context):
    await update.message.reply_text(update.message.text)

BOT_CTRL_INDEX = {
    'start': start,
    'help': help,
    'echo': echo,
    'error': error,
}

