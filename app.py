import streamlit as st
from PIL import Image

# Configuración general de la app
st.set_page_config(page_title="App Multimodal", layout="centered")

# 🌈 Título visual
st.markdown("# 🌈 Bienvenido a mi primera App Multimodal 🎧👁️✋")
st.markdown("Esta aplicación te permitirá explorar diferentes *modalidades sensoriales* de interacción con interfaces digitales.")

# 📸 Subir imagen o mostrar una por defecto
st.subheader("Carga o muestra una imagen")

uploaded_file = st.file_uploader("📤 Sube una imagen (opcional)", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Tu imagen personalizada", use_container_width=True)
else:
    image = Image.open("Lol.jpg")
    st.image(image, caption="Papu", use_container_width=True)

# ✏️ Entrada de texto
st.subheader("Entrada de texto")
texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es:", f"**{texto}**")

# 📑 Columnas con opciones
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 Primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario.")
    resp = st.checkbox("Estoy de acuerdo")
    if resp:
        st.success("✅ ¡Correcto! Las interfaces multimodales mejoran mucho la UX.")

with col2:
    st.subheader("🎚️ Segunda columna")
    modo = st.radio(
        "¿Qué modalidad es la principal en tu interfaz?",
        ("Visual", "Auditiva", "Táctil")
    )
    if modo == "Visual":
        st.info("👁️ La vista es fundamental para tu interfaz.")
    elif modo == "Auditiva":
        st.info("🎧 La audición es fundamental para tu interfaz.")
    elif modo == "Táctil":
        st.info("✋ El tacto es fundamental para tu interfaz.")

# 🔘 Botón interactivo
st.subheader("Uso de Botones")
if st.button("Por favor amigo oprime este botón"):
    st.success("🙌 ¡Gracias por oprimirme!")
else:
    st.warning("🫠 Aún no has presionado el botón...")

# 📦 Selectbox
st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico")
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write("🎯 La acción es:", f"**{set_mod}**")

# 💬 Área de comentarios
st.subheader("💭 Deja tus comentarios sobre la app:")
comentario = st.text_area("Escribe tus impresiones, sugerencias o ideas aquí:")

if comentario:
    st.success("📝 ¡Gracias por tu comentario!")
    st.write("Tu comentario fue:")
    st.write(f"“{comentario}”")

# 🧭 Sidebar
with st.sidebar:
    st.header("⚙️ Configuración")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica")
    )
    st.write(f"Has seleccionado la modalidad: **{mod_radio}**")
