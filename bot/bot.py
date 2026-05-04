from telegram.ext import ApplicationBuilder, CommandHandler
from core.parser import parse_input
from core.optimization import optimize
from core.calculations import stress
from core.ai import suggest
from cad.onshape import update_cad
from viz.graph import generate_graph
import os

TOKEN = os.getenv("TOKEN")

async def design(update, context):
    text = " ".join(context.args)
    params = parse_input(text)

    force = params.get("force", 1000)

    w, t = optimize(force)
    s = stress(force, w, t)

    cad_link = update_cad(100, w, t)

    generate_graph()

    msg = f"""
✅ Design Completed

Width = {w} mm
Thickness = {t} mm
Stress = {round(s,2)}

CAD: {cad_link}
Suggestion: {suggest(s)}
"""

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("design", design))

app.run_polling()
