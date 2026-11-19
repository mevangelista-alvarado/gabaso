import streamlit as st
from datetime import datetime
import time
import os
import json
import re
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv(override=True)

# Configuración de la página
st.set_page_config(
    page_title="Para Gabriela Bailón Solano 💙",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado con paleta azul
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    .stApp {
        background: linear-gradient(180deg, #e0f2fe 0%, #bae6fd 25%, #7dd3fc 50%, #38bdf8 75%, #0ea5e9 100%);
    }
    
    .header-container {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(30, 64, 175, 0.3);
        text-align: center;
    }
    
    .header-title {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-subtitle {
        color: #dbeafe;
        font-size: 1.5rem;
        font-weight: 300;
    }
    
    .message-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        box-shadow: 0 5px 20px rgba(30, 64, 175, 0.15);
        border-left: 5px solid #3b82f6;
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .baby-message {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #2563eb;
    }
    
    .husband-message {
        background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
        border-left: 5px solid #4f46e5;
    }
    
    .timeline-container {
        position: relative;
        padding: 3rem 2rem;
        margin: 2rem 0;
        background: white;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(30, 64, 175, 0.15);
    }
    
    .timeline-line {
        position: absolute;
        top: 80px;
        left: 2rem;
        right: 2rem;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6 0%, #60a5fa 50%, #93c5fd 100%);
        border-radius: 2px;
        z-index: 1;
    }
    
    .timeline-bullet {
        width: 35px;
        height: 35px;
        background: #3b82f6;
        border: 4px solid white;
        border-radius: 50%;
        box-shadow: 0 0 0 3px #3b82f6, 0 3px 10px rgba(30, 64, 175, 0.3);
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        z-index: 2;
        margin: 0 auto 0.5rem auto;
    }
    
    .timeline-bullet:hover {
        transform: scale(1.3);
        background: #2563eb;
        box-shadow: 0 0 0 5px #2563eb, 0 5px 15px rgba(30, 64, 175, 0.5);
    }
    
    .timeline-bullet.active {
        background: #1e40af;
        box-shadow: 0 0 0 5px #1e40af, 0 5px 20px rgba(30, 64, 175, 0.6);
        transform: scale(1.4);
    }
    
    /* Estilo para los botones de timeline */
    button[data-testid*="timeline_btn"] {
        background: rgba(59, 130, 246, 0.1) !important;
        border: 2px solid #dbeafe !important;
        color: #1e40af !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
        margin-top: 0.5rem !important;
    }
    
    button[data-testid*="timeline_btn"]:hover {
        background: rgba(59, 130, 246, 0.2) !important;
        border-color: #3b82f6 !important;
        transform: translateY(-2px);
        box-shadow: 0 3px 10px rgba(30, 64, 175, 0.2) !important;
    }
    
    .timeline-year-label {
        color: #1e40af;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 0.5rem;
        text-align: center;
    }
    
    .timeline-content {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        box-shadow: 0 5px 20px rgba(30, 64, 175, 0.15);
        border: 2px solid #dbeafe;
        animation: fadeIn 0.5s ease-in;
    }
    
    .timeline-content-year {
        color: #1e40af;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .timeline-content-event {
        color: #3b82f6;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .timeline-content-text {
        color: #1e3a8a;
        font-size: 1.1rem;
        line-height: 1.8;
    }
    
    .pin-container {
        max-width: 400px;
        margin: 5rem auto;
        padding: 3rem;
        background: white;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(30, 64, 175, 0.2);
    }
    
    .heart {
        color: #ef4444;
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .baby-icon {
        font-size: 2rem;
        margin-right: 0.5rem;
    }
    
    .message-image {
        width: 100%;
        max-width: 500px;
        border-radius: 15px;
        margin: 1rem auto;
        display: block;
        box-shadow: 0 5px 15px rgba(30, 64, 175, 0.2);
    }
    
    .music-player-container {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        box-shadow: 0 5px 20px rgba(30, 64, 175, 0.15);
        border: 2px solid #dbeafe;
    }
    
    .music-player-title {
        color: #1e40af;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-align: center;
    }

    .coupon-card {
        background: linear-gradient(160deg, #ffffff 0%, #eff6ff 100%);
        border: 2px dashed #3b82f6;
        border-radius: 16px;
        padding: 1.1rem 1.2rem 1rem 1.2rem;
        margin: 0.4rem 0 0.8rem 0;
        box-shadow: 0 4px 14px rgba(30, 64, 175, 0.12);
        min-height: 180px;
    }

    .coupon-emoji {
        font-size: 1.8rem;
        margin-bottom: 0.2rem;
    }

    .coupon-title {
        color: #1e40af;
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0.15rem 0 0.4rem 0;
    }

    .coupon-text {
        color: #1e3a8a;
        font-size: 0.98rem;
        line-height: 1.55;
        margin: 0;
    }

    .coupon-valid {
        color: #2563eb;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.7rem;
    }
    </style>
""", unsafe_allow_html=True)

# PIN de acceso desde variable de entorno
CORRECT_PIN = os.getenv("APP_PIN")

# Inicializar sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Función de autenticación
def check_pin(pin):
    return pin == CORRECT_PIN

# Página de login
if not st.session_state.authenticated:
    st.markdown("""
        <div class="pin-container">
            <h1 style="text-align: center; color: #1e40af; margin-bottom: 2rem;">
                💙 Acceso Especial para mi chaparryta hermosa 💙
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        pin_input = st.text_input("Ingresa el PIN especial:", type="password", key="pin")
        
        if st.button("✨ Entrar ✨", use_container_width=True, type="primary"):
            if check_pin(pin_input):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("PIN incorrecto. Intenta de nuevo.")
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.stop()

# Contenido principal (solo visible si está autenticado)
if st.session_state.authenticated:
    # Reproductor de música automático
    
    # Función para detectar si es una URL de YouTube
    def is_youtube_url(url):
        youtube_domains = ['youtube.com', 'youtu.be', 'youtube-nocookie.com']
        return any(domain in url.lower() for domain in youtube_domains)
    
    # Función para extraer el ID de video de YouTube
    def extract_youtube_id(url):
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com\/watch\?.*v=([a-zA-Z0-9_-]{11})'
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    # Función para convertir URL de YouTube a formato embed
    def youtube_to_embed(url):
        video_id = extract_youtube_id(url)
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}?autoplay=1&rel=0&modestbranding=1"
        return None
    
    # Lista de canciones (playlist)
    playlist = []
    
    # Opción 1: Cargar desde archivo JSON (recomendado)
    playlist_file_json = "playlist.json"
    if os.path.exists(playlist_file_json):
        try:
            with open(playlist_file_json, 'r', encoding='utf-8') as f:
                playlist_data = json.load(f)
                if isinstance(playlist_data, list):
                    playlist.extend(playlist_data)
                elif isinstance(playlist_data, dict) and 'songs' in playlist_data:
                    playlist.extend(playlist_data['songs'])
        except Exception as e:
            st.warning(f"No se pudo cargar playlist.json: {e}")
    
    # Opción 2: Cargar desde archivo de texto simple (una URL por línea)
    playlist_file_txt = "playlist.txt"
    if os.path.exists(playlist_file_txt):
        try:
            with open(playlist_file_txt, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):  # Ignorar líneas vacías y comentarios
                        # Si solo tiene el ID, convertir a URL completa
                        if len(line) == 11 and line.replace('-', '').replace('_', '').isalnum():
                            playlist.append(f"https://www.youtube.com/watch?v={line}")
                        elif 'youtube.com' in line or 'youtu.be' in line:
                            playlist.append(line)
                        elif line.startswith('http'):
                            playlist.append(line)
        except Exception as e:
            st.warning(f"No se pudo cargar playlist.txt: {e}")
    
    # Opción 3: Agregar directamente en el código (para casos especiales)
    # Descomenta y agrega tus URLs aquí:
    # playlist.append("https://www.youtube.com/watch?v=hm8kJQf7ShY")
    # playlist.append("https://www.youtube.com/watch?v=OTRO_ID")
    
    # Si hay archivos locales en una carpeta 'music', los agregamos
    music_folder = "music"
    if os.path.exists(music_folder):
        for file in sorted(os.listdir(music_folder)):
            if file.endswith(('.mp3', '.wav', '.ogg', '.m4a')):
                file_path = os.path.join(music_folder, file)
                # Para archivos locales, necesitamos la ruta relativa
                playlist.append(file_path)
    
    # Eliminar duplicados manteniendo el orden
    seen = set()
    playlist_unique = []
    for song in playlist:
        # Normalizar URLs de YouTube para comparar
        if is_youtube_url(song):
            video_id = extract_youtube_id(song)
            if video_id:
                if video_id not in seen:
                    seen.add(video_id)
                    playlist_unique.append(song)
            else:
                if song not in seen:
                    seen.add(song)
                    playlist_unique.append(song)
        else:
            if song not in seen:
                seen.add(song)
                playlist_unique.append(song)
    
    playlist = playlist_unique
    
    # Si hay canciones en la playlist, crear el reproductor automático
    if playlist:
        # Inicializar el índice de la canción actual
        if 'current_song_index' not in st.session_state:
            st.session_state.current_song_index = 0
        
        current_song = playlist[st.session_state.current_song_index]
        is_youtube = is_youtube_url(current_song)
        
        # Obtener nombre de la canción
        if is_youtube:
            video_id = extract_youtube_id(current_song)
            song_name = f"YouTube Video ({video_id[:8]}...)" if video_id else "YouTube Video"
        else:
            song_name = os.path.basename(current_song) if os.path.isfile(current_song) else f"Canción {st.session_state.current_song_index + 1}"
        
        # Crear reproductor HTML5 con JavaScript para reproducción automática y cambio de canción
        playlist_json = json.dumps(playlist)
        
        # Si es YouTube, mostrar reproductor en un expander
        if is_youtube:
            embed_url = youtube_to_embed(current_song)
            video_id = extract_youtube_id(current_song)
            if embed_url:
                # Iframe oculto pero siempre cargado (para que funcione el JavaScript)
                st.markdown(f"""
                    <div id="hiddenYoutubeContainer" style="position: fixed; bottom: -1000px; left: -1000px; width: 1px; height: 1px; opacity: 0.01; pointer-events: none; z-index: -1;">
                        <iframe id="youtubeIframe" src="{embed_url}?enablejsapi=1" style="width: 1px; height: 1px; border: none;"></iframe>
                    </div>
                """, unsafe_allow_html=True)
                
                # Controles de navegación siempre visibles
                st.markdown(f"""
                    <style>
                    .song-info-display {{
                        background: white;
                        padding: 1rem;
                        border-radius: 15px;
                        box-shadow: 0 3px 15px rgba(30, 64, 175, 0.1);
                        margin: 1rem 0;
                        text-align: center;
                        color: #1e40af;
                        font-weight: 600;
                        font-size: 1.2rem;
                    }}
                    </style>
                    <!--<div class="song-info-display">
                        🎵 {song_name} ({st.session_state.current_song_index + 1} de {len(playlist)})
                    </div>-->
                """, unsafe_allow_html=True)
                
                # Estado para controlar play/pause
                if 'youtube_should_play' not in st.session_state:
                    st.session_state.youtube_should_play = True
                if 'youtube_should_pause' not in st.session_state:
                    st.session_state.youtube_should_pause = False
                
                # Botones de Streamlit
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    if st.button("⏮️ Anterior", use_container_width=True):
                        st.session_state.current_song_index = (st.session_state.current_song_index - 1) % len(playlist)
                        # Reiniciar estado de play/pause al cambiar de canción
                        st.session_state.youtube_should_play = True
                        st.session_state.youtube_should_pause = False
                        st.rerun()
                with col2:
                    # Determinar el texto del botón basado en el estado
                    should_play = st.session_state.youtube_should_play and not st.session_state.youtube_should_pause
                    button_text = "⏸️ Pausar" if should_play else "▶️ Reproducir"
                    
                    if st.button(button_text, use_container_width=True, key="play_pause_btn"):
                        if should_play:
                            st.session_state.youtube_should_pause = True
                            st.session_state.youtube_should_play = False
                        else:
                            st.session_state.youtube_should_play = True
                            st.session_state.youtube_should_pause = False
                        st.rerun()
                with col3:
                    if st.button("⏭️ Siguiente", use_container_width=True):
                        st.session_state.current_song_index = (st.session_state.current_song_index + 1) % len(playlist)
                        # Reiniciar estado de play/pause al cambiar de canción
                        st.session_state.youtube_should_play = True
                        st.session_state.youtube_should_pause = False
                        st.rerun()
                
                # Script de YouTube API (siempre cargado)
                st.markdown(f"""
                    <script src="https://www.youtube.com/iframe_api"></script>
                    <script>
                        var player;
                        var isPlaying = false;
                        
                        function onYouTubeIframeAPIReady() {{
                            console.log('Inicializando reproductor de YouTube');
                            player = new YT.Player('youtubeIframe', {{
                                events: {{
                                    'onReady': onPlayerReady,
                                    'onStateChange': onPlayerStateChange
                                }}
                            }});
                        }}
                        
                        function onPlayerReady(event) {{
                            console.log('Reproductor listo');
                            
                            // Leer el estado de Streamlit y controlar el reproductor
                            const shouldPlay = {str(st.session_state.youtube_should_play).lower()};
                            const shouldPause = {str(st.session_state.youtube_should_pause).lower()};
                            
                            console.log('Estado - shouldPlay:', shouldPlay, 'shouldPause:', shouldPause);
                            
                            // Convertir strings a booleanos
                            const shouldPlayBool = shouldPlay === 'true';
                            const shouldPauseBool = shouldPause === 'true';
                            
                            if (shouldPlayBool && !shouldPauseBool) {{
                                try {{
                                    event.target.playVideo();
                                    isPlaying = true;
                                    console.log('Reproduciendo automáticamente');
                                }} catch (e) {{
                                    console.log('Autoplay bloqueado:', e);
                                }}
                            }} else if (shouldPauseBool) {{
                                try {{
                                    event.target.pauseVideo();
                                    isPlaying = false;
                                    console.log('Pausado automáticamente');
                                }} catch (e) {{
                                    console.log('Error al pausar:', e);
                                }}
                            }}
                        }}
                        
                        function onPlayerStateChange(event) {{
                            if (event.data == YT.PlayerState.PLAYING) {{
                                isPlaying = true;
                                console.log('Reproduciendo');
                            }} else if (event.data == YT.PlayerState.PAUSED) {{
                                isPlaying = false;
                                console.log('Pausado');
                            }} else if (event.data == YT.PlayerState.ENDED) {{
                                isPlaying = false;
                                console.log('Video terminado');
                                // Pasar a la siguiente canción
                                const nextIndex = ({st.session_state.current_song_index} + 1) % {len(playlist)};
                                window.location.href = window.location.href.split('?')[0] + '?next=' + nextIndex;
                                setTimeout(() => window.location.reload(), 100);
                            }}
                        }}
                        
                        // Función para cambiar de canción
                        function loadNextSong() {{
                            const nextIndex = ({st.session_state.current_song_index} + 1) % {len(playlist)};
                            window.location.href = window.location.href.split('?')[0] + '?next=' + nextIndex;
                            setTimeout(() => window.location.reload(), 100);
                        }}
                        
                        function loadPrevSong() {{
                            const prevIndex = ({st.session_state.current_song_index} - 1 + {len(playlist)}) % {len(playlist)};
                            window.location.href = window.location.href.split('?')[0] + '?prev=' + prevIndex;
                            setTimeout(() => window.location.reload(), 100);
                        }}
                        
                        // Función para verificar y aplicar el estado después de la inicialización
                        function checkAndApplyState() {{
                            if (!player) {{
                                console.log('Reproductor aún no está listo');
                                return;
                            }}
                            
                            const shouldPlay = {str(st.session_state.youtube_should_play).lower()};
                            const shouldPause = {str(st.session_state.youtube_should_pause).lower()};
                            const shouldPlayBool = shouldPlay === 'true';
                            const shouldPauseBool = shouldPause === 'true';
                            
                            console.log('Verificando estado - shouldPlay:', shouldPlayBool, 'shouldPause:', shouldPauseBool);
                            
                            try {{
                                if (shouldPlayBool && !shouldPauseBool) {{
                                    const playerState = player.getPlayerState();
                                    if (playerState !== YT.PlayerState.PLAYING) {{
                                        player.playVideo();
                                        isPlaying = true;
                                        console.log('Reproduciendo desde checkAndApplyState');
                                    }}
                                }} else if (shouldPauseBool) {{
                                    const playerState = player.getPlayerState();
                                    if (playerState !== YT.PlayerState.PAUSED) {{
                                        player.pauseVideo();
                                        isPlaying = false;
                                        console.log('Pausando desde checkAndApplyState');
                                    }}
                                }}
                            }} catch (e) {{
                                console.error('Error al aplicar estado:', e);
                            }}
                        }}
                        
                        // Hacer funciones globales
                        window.togglePlayPause = togglePlayPause;
                        window.loadNextSong = loadNextSong;
                        window.loadPrevSong = loadPrevSong;
                        window.checkAndApplyState = checkAndApplyState;
                        
                        // Si la API ya está cargada
                        if (typeof YT !== 'undefined' && YT.Player) {{
                            onYouTubeIframeAPIReady();
                        }} else {{
                            window.onYouTubeIframeAPIReady = onYouTubeIframeAPIReady;
                        }}
                        
                        // Verificar el estado después de un breve delay para asegurar que el reproductor esté listo
                        setTimeout(function() {{
                            checkAndApplyState();
                        }}, 2000);
                    </script>
                """, unsafe_allow_html=True)
                
        else:
            # Reproductor de audio normal
            st.markdown(f"""
        <style>
        .audio-controls-container {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin: 1rem 0;
            background: white;
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 0 3px 15px rgba(30, 64, 175, 0.1);
        }}
        
        .audio-nav-button {{
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            border: none;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 3px 10px rgba(30, 64, 175, 0.3);
        }}
        
        .audio-nav-button:hover {{
            transform: scale(1.1);
            box-shadow: 0 5px 15px rgba(30, 64, 175, 0.5);
            background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        }}
        
        .audio-nav-button:active {{
            transform: scale(0.95);
        }}
        
        #audioPlayer {{
            flex: 1;
            height: 50px;
        }}
        
        #songInfo {{
            text-align: center;
            color: #1e40af;
            margin-top: 0.5rem;
            font-weight: 600;
            font-size: 1rem;
        }}
        </style>
        <div style="margin: 1rem 0;">
            <div class="audio-controls-container">
                <button class="audio-nav-button" id="prevButton" onclick="loadPrevSong()" title="Canción anterior">⏮️</button>
                <audio id="audioPlayer" autoplay controls style="flex: 1;">
                    <source src="{current_song}" type="audio/mpeg">
                    Tu navegador no soporta el elemento de audio.
                </audio>
                <button class="audio-nav-button" id="nextButton" onclick="loadNextSong()" title="Siguiente canción">⏭️</button>
            </div>
            <p id="songInfo" style="text-align: center; color: #1e40af; margin-top: 0.5rem; font-weight: 600;">
                🎵 {song_name} ({st.session_state.current_song_index + 1}/{len(playlist)})
            </p>
        </div>
                <script>
            // Variables globales para el reproductor
            window.playlist = {playlist_json};
            window.currentIndex = {st.session_state.current_song_index};
            
            // Función para detectar si es YouTube
            function isYouTube(url) {{
                return url.includes('youtube.com') || url.includes('youtu.be');
            }}
            
            // Función para obtener el nombre de la canción
            function getSongName(index) {{
                const url = window.playlist[index];
                if (isYouTube(url)) {{
                    return 'YouTube Video';
                }}
                const parts = url.split('/');
                const filename = parts[parts.length - 1];
                return filename || `Canción ${{index + 1}}`;
            }}
            
            // Función para actualizar la información de la canción
            function updateSongInfo(index) {{
                const songInfo = document.getElementById('songInfo');
                const songName = getSongName(index);
                if (songInfo) {{
                    songInfo.textContent = `🎵 ${{songName}} (${{index + 1}}/${{window.playlist.length}})`;
                }}
            }}
            
            // Función para cargar una canción específica (solo para audio)
            function loadSong(index) {{
                const audio = document.getElementById('audioPlayer');
                if (!audio || !window.playlist || index < 0 || index >= window.playlist.length) {{
                    console.error('Error: No se puede cargar la canción');
                    return;
                }}
                
                const url = window.playlist[index];
                // Si es YouTube, recargar la página
                if (isYouTube(url)) {{
                    window.location.reload();
                    return;
                }}
                
                window.currentIndex = index;
                audio.src = url;
                audio.load();
                updateSongInfo(index);
                
                // Intentar reproducir
                const playPromise = audio.play();
                if (playPromise !== undefined) {{
                    playPromise.catch(function(error) {{
                        console.log('Error al reproducir:', error);
                    }});
                }}
            }}
            
            // Función para cargar la siguiente canción
            window.loadNextSong = function() {{
                const nextIndex = (window.currentIndex + 1) % window.playlist.length;
                const nextUrl = window.playlist[nextIndex];
                
                // Si la siguiente es YouTube o la actual es YouTube, recargar página
                if (isYouTube(nextUrl) || isYouTube(window.playlist[window.currentIndex])) {{
                    // Necesitamos comunicarnos con Streamlit para cambiar el índice
                    // Por ahora, recargamos la página
                    window.location.href = window.location.href.split('?')[0] + '?next=' + nextIndex;
                    return;
                }}
                
                loadSong(nextIndex);
            }};
            
            // Función para cargar la canción anterior
            window.loadPrevSong = function() {{
                const prevIndex = (window.currentIndex - 1 + window.playlist.length) % window.playlist.length;
                const prevUrl = window.playlist[prevIndex];
                
                // Si la anterior es YouTube o la actual es YouTube, recargar página
                if (isYouTube(prevUrl) || isYouTube(window.playlist[window.currentIndex])) {{
                    window.location.href = window.location.href.split('?')[0] + '?prev=' + prevIndex;
                    return;
                }}
                
                loadSong(prevIndex);
            }};
            
            // Inicializar cuando el DOM esté listo
            document.addEventListener('DOMContentLoaded', function() {{
                const audio = document.getElementById('audioPlayer');
                if (!audio) return;
                
                // Cuando termine la canción actual, cargar la siguiente automáticamente
                audio.addEventListener('ended', function() {{
                    window.loadNextSong();
                }});
                
                // Reproducir automáticamente al cargar
                audio.addEventListener('loadeddata', function() {{
                    const playPromise = audio.play();
                    if (playPromise !== undefined) {{
                        playPromise.catch(function(error) {{
                            console.log('Autoplay bloqueado por el navegador. Haz click en play para reproducir.');
                        }});
                    }}
                }});
                
                // Actualizar la información inicial
                updateSongInfo(window.currentIndex);
            }});
        </script>
        """, unsafe_allow_html=True)
    else:
        st.info("💡 Agrega archivos de música en la carpeta 'music/' o edita el código para agregar URLs de música.")
    
    # Header
    st.markdown("""
        <div class="header-container">
            <div class="header-title">💙 Feliz Cumpleaños Mi Amor 💙</div>
            <div class="header-subtitle">Un regalo especial de Maita y tu danonino</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Storytelling de su historia - Línea de tiempo interactiva al principio
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Nuestra Historia de Amor")
    
    timeline = [
        {
            "year": "2009",
            "event": "Inicio de la historia",
            "description": "Nuestro primer encuentro. Dos almas que se encontraron en la colinia Garita, sin saber que ese sería el inicio de una hermosa amistad."
        },
        {
            "year": "2010",
            "event": "Nuestra historia de amor",
            "description": "Nos hicimos novios en las playas de Acapulco, allí ocurrio nuestro primer beso y comenzamos nuestra historia de amor."
        },
        {
            "year": "2011-2014",
            "event": "Aprendiendo a amar",
            "description": "Maduramos una relación con altas y bajas."
        },
        {
            "year": "2015",
            "event": "Nos mudamos a la CDMX",
            "description": "Empezamos a vivir juntos. El comienzo de construir nuestra vida en común, lleno de sueños y proyectos compartidos."
        },
        {
            "year": "2018",
            "event": "Tu maestría",
            "description": "Completaste tu maestría en la UPN. Un logro increíble que demostró tu dedicación y pasión por crecer academicamente."
        },
        {
            "year": "2019",
            "event": "Mi maestría",
            "description": "Yo también completé mi maestría en la UNAM. Juntos alcanzamos nuestras metas académicas, apoyándonos mutuamente en cada paso."
        },
        {
            "year": "2020",
            "event": "Mi Doctorado",
            "description": "Inicié mi doctorado en la UNAM. Una nueva etapa de crecimiento y aprendizaje, con tu apoyo incondicional a mi lado."
        },
        {
            "year": "2023",
            "event": "La Rosario Castellanos",
            "description": "Inicié a trabajar en la UNRC, gracias a tí."
        },
        {
            "year": "2024",
            "event": "Tu Doctorado",
            "description": "Empezaste tu doctorado en el CECIJUD y empezaste a trabajar en la UNRC. Otro capítulo brillante en tu trayectoria, demostrando una vez más tu increíble determinación."
        },
        {
            "year": "2025",
            "event": "Maita",
            "image": "image/eco_maita.jpeg",
            "description": "La mejor noticia de todas: ¡estamos esperando a Maita! El mayor regalo que la vida nos ha dado. Nuestra familia crece con amor."
        },
        {
            "year": "2026",
            "event": "Llegó Maita",
            "image": "image/maita_y_mama.png",
            "description": "Estos últimos 10 meses con Maita no han sido fáciles. Hemos atravesado etapas difíciles, sobre todo por la cuestión del parto, que nos puso a prueba como nunca. Pero hoy, con Maita entre nosotros, sabemos que cada momento difícil valió la pena, porque de ellos nació algo hermoso: una familia fuerte, unida y muy amorosa. Maita nos ha enseñado a ser más pacientes, más fuertes y a valorar cada sonrisa. Gracias por tu fuerza, tu paciencia y tu amor. Ahora empieza la parte más bonita de nuestra historia, y la vivimos juntos, de la mano, como siempre."
        }
    ]
    
    # Inicializar el índice seleccionado si no existe
    if 'selected_timeline_index' not in st.session_state:
        st.session_state.selected_timeline_index = 0
    
    # Contenedor de la línea de tiempo
    # st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
    
    # Crear la línea con bullets
    num_items = len(timeline)
    cols = st.columns(num_items)
    
    for idx, (col, item) in enumerate(zip(cols, timeline)):
        with col:
            is_active = "active" if idx == st.session_state.selected_timeline_index else ""
            # Contenedor con bullet y año
            st.markdown(f"""
                <div style="position: relative; text-align: center; padding: 0.5rem;">
                    <div class="timeline-bullet {is_active}"></div>
                    <!--<div class="timeline-year-label">{item["year"]}</div>-->
                    <br>
                </div>
            """, unsafe_allow_html=True)
            
            # Botón clicable sobre toda el área
            if st.button(f"📅 {item['year']}", key=f"timeline_btn_{idx}", use_container_width=True):
                st.session_state.selected_timeline_index = idx
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Mostrar el contenido del evento seleccionado
    selected_item = timeline[st.session_state.selected_timeline_index]

    # Foto dentro de la tarjeta (se reduce y se incrusta en base64 para que quede dentro del HTML)
    photo_html = ""
    if selected_item.get('image') and os.path.exists(selected_item['image']):
        import base64
        import io
        from PIL import Image

        @st.cache_data
        def load_card_photo_b64(path, max_width=700):
            img = Image.open(path).convert("RGB")
            img.thumbnail((max_width, max_width))
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=85)
            return base64.b64encode(buf.getvalue()).decode()

        photo_b64 = load_card_photo_b64(selected_item['image'])
        photo_alt = selected_item["event"]
        photo_html = f'<img src="data:image/jpeg;base64,{photo_b64}" class="message-image" alt="{photo_alt}" />'

    # Sin líneas en blanco ni sangría: si no, Streamlit muestra el HTML como texto
    card_parts = [
        '<div class="timeline-content">',
        f'<div class="timeline-content-year">{selected_item["year"]}</div>',
        f'<div class="timeline-content-event">{selected_item["event"]}</div>',
    ]
    if photo_html:
        card_parts.append(photo_html)
    card_parts.append(f'<div class="timeline-content-text">{selected_item["description"]}</div>')
    card_parts.append('</div>')
    st.markdown("".join(card_parts), unsafe_allow_html=True)
    
    # Mensajes de Maita ya nacida (10 meses), escritos desde su perspectiva
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 👶 Mensajes de Maita 👶")

    maita_nacida_messages = [
        {
            "title": "💙 Mamá, Ya Llevo 10 Meses Contigo 💙",
            "text": "Mamita hermosa, ¿sabes? Ya llevo 10 meses contigo y cada día me siento más feliz de estar a tu lado. Al principio no sabía nada del mundo, pero tu voz, tus caricias y tus abrazos me enseñaron que aquí, en tus brazos, es donde yo pertenezco.<br><br>Me encanta cuando me cantas, cuando me platicas cosas aunque todavía no te entienda del todo, y cuando me miras con esos ojos llenos de amor. Siento que cada mañana me recibes con una sonrisa, y eso me hace sentir la bebé más afortunada del mundo.<br><br>Gracias por tu paciencia cuando no puedo dormir, por tus manos que me sostienen y por tu voz que me calma cuando estoy inquieta. Gracias por cuidarme en las noches, por velar mis sueños, por sostenerme cuando lloro y por reír conmigo cuando hago mis ocurrencias. Gracias por cambiarme, alimentarme, abrazarme y no soltarme cuando más lo necesito. Nunca imaginé que el amor pudiera sentirse tan grande y tan cálido.<br><br>Estoy muy feliz de estar contigo, mamá. Eres mi lugar seguro, mi casa, mi mejor compañía y mi heroína favorita. Aunque todavía no sé decir todo lo que siento, quiero que sepas que te agradezco con todo mi corazón por tu amor, por tu tiempo y por hacer de nuestra familia algo tan bonito, tan fuerte y tan lleno de cariño.<br><br>Te prometo que siempre voy a quererte, a buscarte con la mirada y a llenar tu día de sonrisas. Te quiero muchísimo, mamita. Con todo mi amor y gratitud, te doy el abrazo más grande que puedo."
        },
        {
            "title": "🌟 Chiquita Pero Muy Lista y Traviesa 🌟",
            "text": "Mamá, sé que a veces te preocupas porque todavía soy muy chiquita, y quiero que sepas que estoy echándole muchísimas ganas a crecer. Cada día aprendo algo nuevo: a intentar caminar, a agarrar mis juguetes, a mirar con curiosidad todo lo que me rodea.<br><br>No te preocupes por mi tamaño. Puede que sea pequeña, pero tengo una mente muy inteligente y un corazón muy valiente. Ya me doy cuenta de muchas cosas, y estoy segura de que pronto voy a sorprenderte con todo lo que puedo hacer.<br><br>También soy muy traviesa, lo sé. Me gusta tirar las cosas para ver qué pasa y reírme cuando me miras con cara de sorpresa. ¡Ya tengo muchos planes para nuestras aventuras!<br><br>Imagina todo lo que vamos a explorar juntas: parques llenos de árboles, cuentos antes de dormir, días de playa y comer arena. Tú me vas a enseñar el mundo, y yo te voy a enseñar a sonreír todavía más.<br><br>Así que tranquila, mamá. Yo ya estoy lista para vivir mil aventuras contigo."
        }
    ]

    for msg in maita_nacida_messages:
        with st.expander(f"**{msg['title']}**", expanded=False):
            st.markdown(f"""
                <div class="message-card baby-message">
                    <p style="color: #1e3a8a; font-size: 1.1rem; line-height: 1.8;">{msg['text']}</p>
                    <p style="color: #1e40af; font-size: 1.3rem; font-weight: 600; margin-top: 1.5rem; text-align: center;">
                        Con todo mi amor, Maita 💙
                    </p>
                </div>
            """, unsafe_allow_html=True)

    # Mensaje del esposo
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🦖 Mensajes de danonino 🦖")
    
    esposo_messages = [
        {
            "title": "💕 Para Mi Esposa, Mi Todo 💕",
            "text": """Mi amor, en este día tan especial quiero decirte que soy el hombre más feliz y bendecido del mundo. Tenerte como mi esposa sigue siendo el mayor regalo que la vida me ha dado, y ahora, con Maita ya entre nosotros, con sus 10 meses de risas, travesuras y noches largas, esa felicidad se multiplica todos los días.<br>
                       <br>Estos meses no han sido fáciles. El parto nos puso a prueba y hubo etapas duras, pero verte cuidar de nuestra hija, con esa fuerza y ese amor tan grande, me llena de orgullo. Gracias por ser la mamá de Maita, por no soltarnos y por seguir siendo mi casa.<br>
                       <br>Te amo más de lo que las palabras pueden expresar. Feliz cumpleaños, mi vida. Que este nuevo año esté lleno de salud, descanso y felicidad para las tres.
                    """,
            #"image": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=500&h=400&fit=crop"
        }
    ]

    for msg in esposo_messages:
        with st.expander(f"**{msg['title']}**", expanded=False):
            # Mostrar imagen si existe
            if msg.get('image'):
                st.image(msg['image'], use_container_width=True, caption="")
            st.markdown(f"""
                <div class="message-card husband-message">
                    <p style="color: #1e3a8a; font-size: 1.2rem; line-height: 2;">{msg['text']}</p>
                    <p style="color: #1e40af; font-size: 1.3rem; font-weight: 600; margin-top: 1.5rem; text-align: center;">
                        Con todo mi amor, tu esposo 💙
                    </p>
                </div>
            """, unsafe_allow_html=True)

    cupones = [
        ("💆", "Masaje de media hora", "Un masaje lento, sin prisa y con las manos de danonino. Tú solo te acuestas y respiras."),
        ("⏳", "Tiempo libre", "Yo me quedo con Maita. Tú sales, lees, caminas o no haces absolutamente nada. Mínimo una hora."),
        ("🧀", "Chetos o papitas de emergencia", "Los chetos o papitas que se te antojen, el día que se te antoje. Yo lo consigo y te lo llevo."),
        ("🍳", "Desayuno en la cama", "Café, algo rico y cero prisa. Yo lo preparo. Tú solo despiertas y lo disfrutas."),
        ("😴", "Siesta protegida", "Mientras tú duermes, yo cuido a Maita. Nadie te despierta hasta que tú quieras."),
        ("🤗", "Abrazo sin límite", "Un abrazo largo, de esos que no se sueltan hasta que tú digas que ya."),
    ]

    with st.expander("**🎟️ Tu cuponera de cumpleaños 🎟️**", expanded=False):
        st.markdown(
            '<p style="color: #1e3a8a; font-size: 1.05rem; line-height: 1.7; margin-bottom: 0.6rem;">'
            "Mi amor, estos cupones no se vencen. Los canjeas cuando quieras, con una mirada, un mensaje o simplemente diciendo “danonino, este”."
            "</p>",
            unsafe_allow_html=True,
        )
        for i in range(0, len(cupones), 2):
            cols = st.columns(2)
            for col, (emoji, titulo, texto) in zip(cols, cupones[i:i + 2]):
                with col:
                    st.markdown(
                        f'<div class="coupon-card">'
                        f'<div class="coupon-emoji">{emoji}</div>'
                        f'<div class="coupon-title">{titulo}</div>'
                        f'<p class="coupon-text">{texto}</p>'
                        f'<div class="coupon-valid">Válido todo el año</div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )

    # Mensajes de Maita
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 👶 Mensajes de Maita en el vientre 👶")
    
    maita_messages = [
        {
            "title": "💙 Hola Mamá 💙",
            "text": """Hola mamá hermosa, soy Maita, tu goldi . Quiero que sepas que estoy aquí dentro creciendo con mucho amor y cariño. Cada día me esfuerzo mucho para desarrollarme bien y llegar sana a tí.<br>
                       <br>Sé que a veces puede ser difícil, pero quiero que sepas que estoy muy feliz aquí dentro. Me encanta escuchar tu voz y sentir tu amor. Ya estoy ansiosa por conocerte y estar en tus brazos.<br>
                       <br>Aunque aún no nos conocemos cara a cara, ya te amo muchísimo, mamá. Eres la persona más importante del mundo para mí. Gracias por cuidarme y amarme tanto.<br>
                       <br>Pronto estaremos juntas.<br>
                       <br>Te amo muchísimo, mamá.
                    """,
            "image": "image/eco_maita.jpeg"
        },
        {
            "title": "💪 Estoy Creciendo Fuerte 💪",
            "text": "No te preocupes por nada, mamá. Estoy echando todas mis ganas para crecer fuerte y saludable. Cada latido de tu corazón me da fuerza, y cada pensamiento de amor que me envías me llena de energía.",
            #"image": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?w=500&h=400&fit=crop"
        },
        {
            "title": "🌟 Mi Futuro Contigo 🌟",
            "text": """Estoy emocionada por todas las aventuras que viviremos juntas. Quiero hacerte reír, darte abrazos, y llenar tu vida de alegría.<br>
                       <br>Eres la mejor mamá del mundo y no puedo esperar a estar contigo.
                    """,
            #"image": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?w=500&h=400&fit=crop"
        }
    ]
    
    for msg in maita_messages:
        with st.expander(f"**{msg['title']}**", expanded=False):
            # Mostrar imagen si existe
            if msg.get('image'):
                st.image(msg['image'], use_container_width=True, caption="")
            st.markdown(f"""
                <div class="message-card baby-message">
                    <p style="color: #1e3a8a; font-size: 1.1rem; line-height: 1.8;">{msg['text']}</p>
                    <p style="color: #1e40af; font-size: 1.3rem; font-weight: 600; margin-top: 1.5rem; text-align: center;">
                        Con todo mi amor, Maita 💙
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    # Imagen del mensaje del esposo
    #husband_image = "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=500&h=400&fit=crop"
    #st.image(husband_image, use_container_width=True, caption="")
    
    #st.markdown("""
    #    <div class="message-card husband-message">
    #        <h3 style="color: #1e40af; margin-bottom: 1rem;">💕 Para Mi Esposa, Mi Todo 💕</h3>
    #        <p style="color: #1e3a8a; font-size: 1.2rem; line-height: 2;">
    #            Mi amor, en este día tan especial quiero decirte que soy el hombre más feliz y bendecido del mundo. 
    #            Tenerte como mi esposa es el mayor regalo que la vida me ha dado, y ahora, con Maita en camino, 
    #            mi felicidad se multiplica infinitamente.
    #        </p>
    #        <p style="color: #1e3a8a; font-size: 1.2rem; line-height: 2; margin-top: 1rem;">
    #            Gracias por darme la dicha de ser el papá de nuestra hija. Gracias por ser tan fuerte, tan amorosa, 
    #            y tan increíble. Ver cómo cuidas de Maita y de nosotros me llena de orgullo y admiración.
    #        </p>
    #        <p style="color: #1e3a8a; font-size: 1.2rem; line-height: 2; margin-top: 1rem;">
    #            Te amo más de lo que las palabras pueden expresar. Feliz cumpleaños, mi vida. Que este nuevo año 
    #           esté lleno de amor, salud y felicidad para las tres.
    #        </p>
    #        <p style="color: #1e40af; font-size: 1.3rem; font-weight: 600; margin-top: 1.5rem; text-align: center;">
    #            Con todo mi amor, tu esposo 💙
    #        </p>
    #    </div>
    #""", unsafe_allow_html=True)
    #
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; padding: 2rem; color: #1e40af;">
            <p style="font-size: 1.2rem; font-weight: 600;">
                💙 Con todo nuestro amor 💙
            </p>
            <p style="font-size: 1rem; margin-top: 0.5rem;">
                Maita y tu esposo
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Botón para cerrar sesión (opcional)
    if st.button("🔒 Cerrar Sesión", use_container_width=False):
        st.session_state.authenticated = False
        st.rerun()

