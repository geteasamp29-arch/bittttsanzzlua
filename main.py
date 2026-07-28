import os
import discord
from discord.ext import commands
from datetime import datetime

# Ambil token otomatis dari Railway Variables
TOKEN = os.getenv("DISCORD_TOKEN")

# Pengaturan dasar bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Fungsi pembuat kerangka script Monetloader
def buat_script_monetloader(nama_script, cmd_utama, fitur_tambahan=""):
    kerangka = f"""-- ==============================================
-- Script Monetloader GTA SAMP
-- Nama: {nama_script}
-- Dibuat otomatis oleh Bot Discord
-- Waktu: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
-- ==============================================

local monet = require "monetloader"

-- Pengaturan
local config = {{
    command = "{cmd_utama}",
    aktif = true,
    versi = "1.0"
}}

-- Fungsi Utama
function mulai()
    if not config.aktif then return end
    monet.print("[INFO] Script "..config.nama.." berjalan!")
    -- Isi kode kamu di bawah ini
    {fitur_tambahan}
end

-- Daftar Perintah
monet.addCommand(config.command, function(pemain, arg)
    mulai()
    return true
end)

-- Muat otomatis saat Monetloader nyala
addEventHandler("onClientResourceStart", root, function(res)
    if getResourceName(res) == "monetloader" then
        mulai()
    end
end)

-- Anti-AWK bawaan
taskSpawn(function()
    while true do
        wait(30000)
        setPedAnalogControlMode(localPed, 0, 0)
    end
end)

monet.print("[BERHASIL] Script siap dipakai!")
"""
    nama_file = f"{nama_script.replace(' ','_')}.lua"
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write(kerangka)
    return nama_file

# Saat bot nyala
@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} AKTIF - Siap buat script Monetloader")
    await bot.change_presence(activity=discord.Game("!buatscript Nama /perintah"))

# Perintah utama buat script
@bot.command(name="buatscript")
async def cmd_buat(ctx, nama_script, cmd_utama, *, tambahan="-- Tanpa fitur tambahan khusus"):
    await ctx.send(f"🔧 Sedang merakit script: **{nama_script}**...")
    file_hasil = buat_script_monetloader(nama_script, cmd_utama, tambahan)
    await ctx.send(
        f"✅ Selesai!\nPerintah: `{cmd_utama}`\n⚠️ Cek ulang isi script sebelum dipakai!",
        file=discord.File(file_hasil)
    )

# Panduan singkat
@bot.command(name="panduan")
async def cmd_panduan(ctx):
    teks = """📖 Cara Pakai:
`!buatscript [NamaScript] [/perintah] [opsi: kode tambahan]`
Contoh:
`!buatscript AutoMancing /mancing`
`!buatscript AutoLogin /login -- print("Masuk otomatis")`
"""
    await ctx.send(teks)

# Cek keamanan
@bot.command(name="ceksamankah")
async def cmd_aman(ctx):
    await ctx.send("⚠️ Bot hanya membuat kerangka kode.\nKamu wajib memeriksa ulang isinya, hindari script sumber tidak jelas!")

# Jalankan bot
bot.run(TOKEN)
