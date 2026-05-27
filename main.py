import streamlit as st
import streamlit.components.v1 as components
import random
import html
from datetime import datetime

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="MBTI 포켓몬 연구소",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# MBTI별 포켓몬 데이터
# =========================
POKEMON_DATA = {
    "INTJ": {
        "pokemon": "뮤츠",
        "id": 150,
        "emoji": "🧠",
        "vibe": "전략가 포켓몬",
        "types": ["에스퍼"],
        "color": "#8E7CC3",
        "catch": "계획은 이미 10수 앞까지 끝났다.",
        "reasons": [
            "깊게 생각하고 큰 그림을 보는 타입이에요.",
            "혼자만의 시간 속에서 아이디어를 강하게 발전시켜요.",
            "목표가 생기면 조용하지만 압도적인 집중력을 보여줘요."
        ],
        "study": "공부할 때는 먼저 전체 단원 구조를 파악한 뒤 세부 내용을 정리해보세요.",
        "friends": ["INFJ", "ENTJ", "INTP"],
        "stats": {"전략력": 98, "집중력": 94, "친화력": 61, "즉흥력": 45}
    },
    "INTP": {
        "pokemon": "폴리곤Z",
        "id": 474,
        "emoji": "💻",
        "vibe": "호기심 폭발 포켓몬",
        "types": ["노말"],
        "color": "#6FA8DC",
        "catch": "왜 그런지 궁금하면 끝까지 파본다!",
        "reasons": [
            "논리적이고 새로운 아이디어를 탐구하는 걸 좋아해요.",
            "남들이 당연하게 넘기는 것도 질문으로 바꿔요.",
            "창의적인 문제 해결 능력이 뛰어나요."
        ],
        "study": "개념을 외우기보다 '왜?'라는 질문을 붙여서 원리를 이해해보세요.",
        "friends": ["ENTP", "INTJ", "INFP"],
        "stats": {"전략력": 89, "집중력": 82, "친화력": 58, "즉흥력": 77}
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "id": 6,
        "emoji": "🔥",
        "vibe": "리더십 화염 포켓몬",
        "types": ["불꽃", "비행"],
        "color": "#E06666",
        "catch": "목표? 좋다. 바로 날아간다.",
        "reasons": [
            "목표를 정하면 강하게 밀고 나가는 추진력이 있어요.",
            "팀을 이끌거나 계획을 세우는 데 강점이 있어요.",
            "도전적인 상황에서 에너지가 더 살아나요."
        ],
        "study": "공부 계획표를 세우고 성취율을 체크하면 동기부여가 크게 올라가요.",
        "friends": ["INTJ", "ENFJ", "ESTJ"],
        "stats": {"전략력": 95, "집중력": 88, "친화력": 76, "즉흥력": 72}
    },
    "ENTP": {
        "pokemon": "로토무",
        "id": 479,
        "emoji": "⚡",
        "vibe": "아이디어 번쩍 포켓몬",
        "types": ["전기", "고스트"],
        "color": "#F1C232",
        "catch": "재밌는 생각이 났어! 일단 해보자!",
        "reasons": [
            "새로운 아이디어를 빠르게 떠올리는 타입이에요.",
            "토론과 실험을 통해 더 좋은 답을 찾아가요.",
            "틀에 박힌 방식보다 색다른 방법을 선호해요."
        ],
        "study": "친구에게 개념을 설명하거나 토론하면서 공부하면 기억에 오래 남아요.",
        "friends": ["INTP", "ENFP", "ESTP"],
        "stats": {"전략력": 84, "집중력": 68, "친화력": 84, "즉흥력": 96}
    },
    "INFJ": {
        "pokemon": "가디안",
        "id": 282,
        "emoji": "🌙",
        "vibe": "따뜻한 통찰 포켓몬",
        "types": ["에스퍼", "페어리"],
        "color": "#B4A7D6",
        "catch": "조용하지만 누구보다 깊게 바라본다.",
        "reasons": [
            "사람의 마음과 분위기를 섬세하게 읽는 편이에요.",
            "이상과 가치관을 중요하게 생각해요.",
            "겉으로는 차분하지만 내면은 매우 깊어요."
        ],
        "study": "배운 내용을 나만의 의미와 연결해 정리하면 이해도가 높아져요.",
        "friends": ["ENFJ", "INFP", "INTJ"],
        "stats": {"전략력": 87, "집중력": 91, "친화력": 88, "즉흥력": 54}
    },
    "INFP": {
        "pokemon": "님피아",
        "id": 700,
        "emoji": "🎀",
        "vibe": "감성 힐링 포켓몬",
        "types": ["페어리"],
        "color": "#EA9999",
        "catch": "내 마음이 반짝이는 방향으로 갈래.",
        "reasons": [
            "상상력이 풍부하고 감정 표현이 섬세해요.",
            "자신만의 가치와 취향을 중요하게 여겨요.",
            "따뜻한 공감 능력으로 주변을 편안하게 해줘요."
        ],
        "study": "딱딱한 암기보다 예시, 이야기, 이미지로 연결해서 공부해보세요.",
        "friends": ["ENFP", "INFJ", "INTP"],
        "stats": {"전략력": 70, "집중력": 78, "친화력": 89, "즉흥력": 74}
    },
    "ENFJ": {
        "pokemon": "망나뇽",
        "id": 149,
        "emoji": "🌈",
        "vibe": "다정한 리더 포켓몬",
        "types": ["드래곤", "비행"],
        "color": "#F6B26B",
        "catch": "다 같이 잘되면 제일 좋잖아!",
        "reasons": [
            "주변 사람들을 챙기고 이끄는 힘이 있어요.",
            "분위기를 부드럽게 만들고 협력을 잘 이끌어요.",
            "목표를 향해 사람들과 함께 나아가는 걸 좋아해요."
        ],
        "study": "스터디 그룹에서 설명하는 역할을 맡으면 학습 효과가 커져요.",
        "friends": ["INFJ", "ESFJ", "ENTJ"],
        "stats": {"전략력": 82, "집중력": 80, "친화력": 97, "즉흥력": 70}
    },
    "ENFP": {
        "pokemon": "토게키스",
        "id": 468,
        "emoji": "✨",
        "vibe": "행운 전파 포켓몬",
        "types": ["페어리", "비행"],
        "color": "#FFD966",
        "catch": "오늘도 반짝이는 가능성 발견!",
        "reasons": [
            "밝고 자유로운 에너지로 주변을 즐겁게 해요.",
            "새로운 사람, 새로운 경험, 새로운 아이디어를 좋아해요.",
            "상상력과 공감력이 함께 강한 타입이에요."
        ],
        "study": "짧은 집중 구간을 여러 번 반복하고, 공부 보상을 정해두면 좋아요.",
        "friends": ["INFP", "ENTP", "ESFP"],
        "stats": {"전략력": 69, "집중력": 66, "친화력": 95, "즉흥력": 94}
    },
    "ISTJ": {
        "pokemon": "메타그로스",
        "id": 376,
        "emoji": "🛡️",
        "vibe": "철벽 계획 포켓몬",
        "types": ["강철", "에스퍼"],
        "color": "#76A5AF",
        "catch": "정확하게, 차근차근, 완벽하게.",
        "reasons": [
            "책임감이 강하고 맡은 일을 꾸준히 해내요.",
            "규칙과 체계를 잘 이해하고 실천해요.",
            "흔들리지 않는 안정감이 장점이에요."
        ],
        "study": "매일 같은 시간에 복습 루틴을 만들면 성적이 안정적으로 올라가요.",
        "friends": ["ESTJ", "ISFJ", "INTJ"],
        "stats": {"전략력": 90, "집중력": 96, "친화력": 63, "즉흥력": 38}
    },
    "ISFJ": {
        "pokemon": "럭키",
        "id": 113,
        "emoji": "🍀",
        "vibe": "다정한 수호 포켓몬",
        "types": ["노말"],
        "color": "#F4CCCC",
        "catch": "조용히 챙겨주는 게 내 방식이야.",
        "reasons": [
            "배려심이 깊고 주변 사람을 세심하게 챙겨요.",
            "성실하고 책임감 있게 일을 마무리해요.",
            "안정적인 환경에서 능력을 잘 발휘해요."
        ],
        "study": "필기 정리와 오답노트를 꾸준히 만들면 큰 효과를 볼 수 있어요.",
        "friends": ["ESFJ", "ISTJ", "ISFP"],
        "stats": {"전략력": 73, "집중력": 92, "친화력": 90, "즉흥력": 42}
    },
    "ESTJ": {
        "pokemon": "윈디",
        "id": 59,
        "emoji": "🏆",
        "vibe": "질서정연 대장 포켓몬",
        "types": ["불꽃"],
        "color": "#CC4125",
        "catch": "할 일은 확실히 끝내야지!",
        "reasons": [
            "현실적이고 실행력이 뛰어나요.",
            "규칙과 목표가 분명할 때 강한 힘을 발휘해요.",
            "주변을 정리하고 이끄는 능력이 좋아요."
        ],
        "study": "할 일을 체크리스트로 만들고 완료 표시를 해보세요.",
        "friends": ["ISTJ", "ENTJ", "ESFJ"],
        "stats": {"전략력": 88, "집중력": 87, "친화력": 74, "즉흥력": 58}
    },
    "ESFJ": {
        "pokemon": "해피너스",
        "id": 242,
        "emoji": "💖",
        "vibe": "분위기 힐러 포켓몬",
        "types": ["노말"],
        "color": "#FFB6C1",
        "catch": "모두가 편하면 나도 행복해.",
        "reasons": [
            "사람들과 어울리며 에너지를 얻어요.",
            "친절하고 분위기를 따뜻하게 만드는 능력이 있어요.",
            "협력 상황에서 장점이 크게 드러나요."
        ],
        "study": "친구들과 서로 문제를 내주며 공부하면 재미와 효율이 올라가요.",
        "friends": ["ISFJ", "ENFJ", "ESTJ"],
        "stats": {"전략력": 70, "집중력": 78, "친화력": 98, "즉흥력": 65}
    },
    "ISTP": {
        "pokemon": "루카리오",
        "id": 448,
        "emoji": "🥷",
        "vibe": "침착한 실전 포켓몬",
        "types": ["격투", "강철"],
        "color": "#3D85C6",
        "catch": "말보다 행동으로 보여준다.",
        "reasons": [
            "문제를 직접 다루며 해결하는 능력이 뛰어나요.",
            "침착하고 상황 판단이 빠른 편이에요.",
            "필요할 때 집중해서 실력을 보여줘요."
        ],
        "study": "문제 풀이를 통해 개념을 익히는 방식이 잘 맞아요.",
        "friends": ["ESTP", "ISFP", "INTP"],
        "stats": {"전략력": 78, "집중력": 81, "친화력": 57, "즉흥력": 85}
    },
    "ISFP": {
        "pokemon": "이브이",
        "id": 133,
        "emoji": "🌸",
        "vibe": "취향 존중 포켓몬",
        "types": ["노말"],
        "color": "#D5A6BD",
        "catch": "내 속도와 내 색깔이 제일 중요해.",
        "reasons": [
            "감각적이고 자신만의 취향이 뚜렷해요.",
            "조용하지만 따뜻한 매력을 가지고 있어요.",
            "가능성이 다양하고 변화에 유연해요."
        ],
        "study": "예쁜 노트 정리, 색깔 표시, 그림 등을 활용하면 집중이 잘돼요.",
        "friends": ["INFP", "ISFJ", "ESFP"],
        "stats": {"전략력": 62, "집중력": 75, "친화력": 82, "즉흥력": 79}
    },
    "ESTP": {
        "pokemon": "초염몽",
        "id": 392,
        "emoji": "🚀",
        "vibe": "스피드 액션 포켓몬",
        "types": ["불꽃", "격투"],
        "color": "#E69138",
        "catch": "일단 부딪혀보면 답이 나온다!",
        "reasons": [
            "활동적이고 상황 대처 능력이 좋아요.",
            "새로운 경험과 도전을 즐기는 편이에요.",
            "빠른 판단과 실행력이 강점이에요."
        ],
        "study": "가만히 오래 앉기보다 시간 제한 문제 풀이처럼 게임화해보세요.",
        "friends": ["ISTP", "ENTP", "ESFP"],
        "stats": {"전략력": 72, "집중력": 64, "친화력": 84, "즉흥력": 98}
    },
    "ESFP": {
        "pokemon": "루브도",
        "id": 235,
        "emoji": "🎨",
        "vibe": "무대 위 아티스트 포켓몬",
        "types": ["노말"],
        "color": "#93C47D",
        "catch": "재밌게 해야 오래 가지!",
        "reasons": [
            "밝고 표현력이 좋아 주변 분위기를 살려요.",
            "현재의 즐거움과 경험을 중요하게 생각해요.",
            "창의적인 방식으로 자신을 드러내는 데 강해요."
        ],
        "study": "공부 내용을 노래, 그림, 카드뉴스처럼 표현해보면 기억에 잘 남아요.",
        "friends": ["ENFP", "ESTP", "ISFP"],
        "stats": {"전략력": 61, "집중력": 60, "친화력": 96, "즉흥력": 93}
    },
}

LUCKY_ITEMS = [
    "반짝이 형광펜 ✨",
    "따뜻한 코코아 ☕",
    "귀여운 스티커팩 🎀",
    "깔끔한 오답노트 📒",
    "집중 타이머 ⏰",
    "달콤한 젤리 🍬",
    "행운의 네잎클로버 🍀",
    "포근한 담요 🧸"
]

TODAY_MISSIONS = [
    "오늘 배운 개념 3개를 한 문장으로 요약하기",
    "틀린 문제 하나를 골라 왜 틀렸는지 설명하기",
    "친구에게 오늘 공부한 내용 1분 설명하기",
    "핵심 키워드 5개로 마인드맵 만들기",
    "내일 공부할 내용 3가지를 미리 적어두기",
    "어려운 개념을 이모지 3개로 표현해보기"
]

FLOATING_EMOJIS = [
    "✨", "🌟", "💫", "⚡", "🔥", "🌈", "🎀", "🍀",
    "💖", "🧸", "🌙", "☁️", "🍓", "🍭", "🎮", "🪄",
    "🥚", "🐣", "🐾", "🫧", "🦄", "🍪", "🎉", "💎"
]

# =========================
# CSS
# =========================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

html, body, [class*="css"] {
    font-family: 'Jua', sans-serif;
}

.stApp {
    background: linear-gradient(-45deg, #fff1f8, #eaf7ff, #f5ecff, #fff8df);
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.main-title {
    text-align: center;
    font-size: 3.2rem;
    color: #ff5fa2;
    text-shadow: 3px 3px 0px #fff, 6px 6px 0px rgba(255, 157, 211, 0.35);
    margin-bottom: 0.2rem;
    animation: popTitle 1.2s ease-in-out infinite alternate;
}

@keyframes popTitle {
    from {transform: scale(1);}
    to {transform: scale(1.025);}
}

.sub-title {
    text-align: center;
    font-size: 1.2rem;
    color: #6b5b95;
    margin-bottom: 2rem;
}

.glass-box {
    background: rgba(255, 255, 255, 0.72);
    border: 2px solid rgba(255, 255, 255, 0.95);
    border-radius: 26px;
    padding: 1.4rem;
    box-shadow: 0 12px 35px rgba(130, 90, 180, 0.18);
    backdrop-filter: blur(8px);
}

.pokemon-card {
    background: rgba(255,255,255,0.86);
    border-radius: 30px;
    padding: 1.5rem;
    border: 4px solid #ffb6d9;
    box-shadow: 0 16px 40px rgba(255, 122, 188, 0.25);
    animation: floatCard 2.5s ease-in-out infinite;
}

@keyframes floatCard {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

.badge {
    display: inline-block;
    padding: 0.35rem 0.75rem;
    border-radius: 999px;
    color: white;
    font-weight: bold;
    margin: 0.15rem;
    background: linear-gradient(135deg, #ff7eb3, #7afcff);
    box-shadow: 0 5px 12px rgba(0,0,0,0.12);
}

.reason-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,245,252,0.9));
    border-left: 8px solid #ff8ac6;
    border-radius: 20px;
    padding: 1rem;
    margin: 0.6rem 0;
    box-shadow: 0 8px 20px rgba(255, 129, 194, 0.16);
}

.small-cute {
    font-size: 0.95rem;
    color: #786fa6;
}

div.stButton > button {
    width: 100%;
    border-radius: 999px;
    border: none;
    color: white;
    font-size: 1.2rem;
    padding: 0.75rem 1rem;
    background: linear-gradient(90deg, #ff70a6, #ff9770, #ffd670, #70d6ff, #b388eb);
    background-size: 300% 300%;
    animation: rainbowButton 3s ease infinite;
    box-shadow: 0 10px 25px rgba(255, 112, 166, 0.35);
}

div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 15px 35px rgba(255, 112, 166, 0.5);
}

@keyframes rainbowButton {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

hr {
    border: none;
    height: 3px;
    background: linear-gradient(90deg, transparent, #ff9bd2, #93d5ff, transparent);
    margin: 2rem 0;
}
</style>
""",
    unsafe_allow_html=True
)

# =========================
# 이모지 효과 컴포넌트
# =========================
def render_floating_emojis():
    particles = ""
    random.seed(datetime.now().strftime("%Y%m%d%H%M"))
    for i in range(42):
        emoji = random.choice(FLOATING_EMOJIS)
        left = random.randint(0, 100)
        delay = random.uniform(0, 5)
        duration = random.uniform(5, 11)
        size = random.randint(20, 38)
        particles += (
            f"<span class='particle' style='left:{left}%; "
            f"animation-delay:{delay}s; animation-duration:{duration}s; "
            f"font-size:{size}px;'>{emoji}</span>"
        )

    components.html(
        f"""
        <style>
        .sparkle-sky {{
            position: relative;
            width: 100%;
            height: 130px;
            overflow: hidden;
            background: transparent;
        }}
        .particle {{
            position: absolute;
            top: 120px;
            opacity: 0;
            animation-name: floatUp;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            filter: drop-shadow(0 4px 4px rgba(0,0,0,0.15));
        }}
        @keyframes floatUp {{
            0% {{
                transform: translateY(0) rotate(0deg) scale(0.8);
                opacity: 0;
            }}
            15% {{
                opacity: 1;
            }}
            80% {{
                opacity: 1;
            }}
            100% {{
                transform: translateY(-160px) rotate(360deg) scale(1.3);
                opacity: 0;
            }}
        }}
        </style>
        <div class="sparkle-sky">
            {particles}
        </div>
        """,
        height=140
    )

def pokemon_sprite_url(pokemon_id):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"

def small_sprite_url(pokemon_id):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"

# =========================
# 사이드바
# =========================
with st.sidebar:
    st.markdown("## 🧪 MBTI 포켓몬 연구소")
    st.markdown(
        """
        이 앱은 MBTI를 선택하면  
        어울리는 포켓몬을 귀엽게 추천해주는  
        **재미용 웹앱**이에요.

        ---
        ### 🛠️ 사용 기술
        - Python
        - Streamlit
        - CSS Animation
        - PokeAPI Sprite 이미지

        ---
        ### 📌 탐구 포인트
        - 딕셔너리 데이터 구조
        - 조건에 따른 화면 출력
        - CSS로 애니메이션 만들기
        - Streamlit Cloud 배포
        """
    )
    st.info("MBTI는 과학적 진단이라기보다 재미용 자기이해 도구로 활용해보세요!")

# =========================
# 메인 화면
# =========================
render_floating_emojis()

st.markdown("<div class='main-title'>✨ MBTI 포켓몬 추천 연구소 ✨</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>너의 성격 타입을 고르면 찰떡 포켓몬 파트너를 찾아줄게! 🐾💖⚡</div>",
    unsafe_allow_html=True
)

if "result_mbti" not in st.session_state:
    st.session_state.result_mbti = None

if "effect_on" not in st.session_state:
    st.session_state.effect_on = True

# 입력 영역
st.markdown("<div class='glass-box'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 1.2, 1])

with col1:
    nickname = st.text_input(
        "트레이너 이름을 입력해줘 🧢",
        placeholder="예: 당곡고 피카츄",
        max_chars=20
    )

with col2:
    selected_mbti = st.selectbox(
        "MBTI를 선택해줘 🔮",
        list(POKEMON_DATA.keys()),
        format_func=lambda x: f"{x}  {POKEMON_DATA[x]['emoji']}  {POKEMON_DATA[x]['vibe']}"
    )

with col3:
    energy = st.slider("오늘의 텐션 ⚡", 1, 100, 77)

st.session_state.effect_on = st.toggle("효과 폭발 모드 ON 🎉", value=st.session_state.effect_on)

clicked = st.button("내 포켓몬 파트너 소환하기! 🪄✨")

st.markdown("</div>", unsafe_allow_html=True)

if clicked:
    st.session_state.result_mbti = selected_mbti
    if st.session_state.effect_on:
        st.balloons()
        if energy >= 80:
            st.snow()

# =========================
# 결과 화면
# =========================
if st.session_state.result_mbti:
    mbti = st.session_state.result_mbti
    data = POKEMON_DATA[mbti]

    safe_name = html.escape(nickname.strip()) if nickname.strip() else "귀여운 트레이너"
    today = datetime.now().strftime("%Y-%m-%d")
    rng = random.Random(f"{safe_name}-{mbti}-{today}")

    lucky_item = rng.choice(LUCKY_ITEMS)
    mission = rng.choice(TODAY_MISSIONS)
    friendship_score = rng.randint(86, 100)
    sparkle_score = rng.randint(70, 100)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style='text-align:center; font-size:1.6rem; color:#ff5fa2;'>
            🎊 {safe_name}님의 MBTI는 <b>{mbti}</b>!  
            운명의 포켓몬 파트너를 발견했어요! 🎊
        </div>
        """,
        unsafe_allow_html=True
    )

    render_floating_emojis()

    left, right = st.columns([1, 1.3])

    with left:
        st.markdown(
            f"""
            <div class='pokemon-card' style='border-color:{data["color"]}; text-align:center;'>
                <div style='font-size:2rem;'>{data["emoji"]}</div>
                <h1 style='margin-bottom:0; color:{data["color"]};'>{data["pokemon"]}</h1>
                <h3 style='margin-top:0.2rem; color:#6b5b95;'>{data["vibe"]}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image(pokemon_sprite_url(data["id"]), use_container_width=True)

    with right:
        badges = " ".join([f"<span class='badge'>{t}</span>" for t in data["types"]])

        st.markdown(
            f"""
            <div class='glass-box'>
                <h2>{data["emoji"]} {mbti}에게 추천하는 포켓몬은?</h2>
                <h1 style='color:{data["color"]};'>{data["pokemon"]}</h1>
                <p style='font-size:1.3rem;'>“{data["catch"]}”</p>
                <div>{badges}</div>
                <br>
                <p>💞 <b>파트너 궁합도:</b> {friendship_score}%</p>
                <p>✨ <b>반짝임 지수:</b> {sparkle_score}%</p>
                <p>🎁 <b>오늘의 행운템:</b> {lucky_item}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 📊 성격 스탯")
        for stat_name, value in data["stats"].items():
            st.progress(value, text=f"{stat_name} {value}%")

    tab1, tab2, tab3, tab4 = st.tabs(["💖 추천 이유", "🤝 찰떡 궁합", "📚 공부 미션", "🎴 미니 카드"])

    with tab1:
        st.markdown("## 💖 왜 이 포켓몬이 어울릴까?")
        for reason in data["reasons"]:
            st.markdown(
                f"""
                <div class='reason-card'>
                    ✨ {reason}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.success(f"📌 학습 팁: {data['study']}")

    with tab2:
        st.markdown("## 🤝 잘 맞는 MBTI 친구 포켓몬")
        friend_cols = st.columns(3)

        for idx, friend_mbti in enumerate(data["friends"]):
            friend = POKEMON_DATA[friend_mbti]
            with friend_cols[idx]:
                st.markdown(
                    f"""
                    <div class='glass-box' style='text-align:center;'>
                        <h3>{friend["emoji"]} {friend_mbti}</h3>
                        <img src='{small_sprite_url(friend["id"])}' width='90'>
                        <h4>{friend["pokemon"]}</h4>
                        <p class='small-cute'>{friend["vibe"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.info("친구들과 서로 MBTI를 입력해서 어떤 포켓몬 조합이 나오는지 비교해보세요!")

    with tab3:
        st.markdown("## 📚 오늘의 공부 미션")
        st.markdown(
            f"""
            <div class='glass-box'>
                <h2>📝 {mission}</h2>
                <p>이 미션을 완료하면 {data["pokemon"]}와의 친밀도가 +10 올라간다는 설정! ✨</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### ⏱️ 추천 공부 루틴")
        if energy >= 80:
            st.write("🔥 오늘 텐션이 높으니까 40분 집중 + 10분 휴식 루틴을 추천해요!")
        elif energy >= 50:
            st.write("🌟 적당한 텐션이에요. 25분 집중 + 5분 휴식 루틴이 좋아요!")
        else:
            st.write("🍵 오늘은 무리하지 말고 15분 집중 + 5분 휴식부터 시작해봐요!")

        check1 = st.checkbox("개념 정리 완료 ✍️")
        check2 = st.checkbox("문제 풀이 완료 🧩")
        check3 = st.checkbox("오답 확인 완료 🔍")

        completed = sum([check1, check2, check3])
        st.progress(completed / 3, text=f"미션 진행률 {completed}/3")

        if completed == 3:
            st.balloons()
            st.success("완벽해요! 오늘의 포켓몬 공부 미션 클리어! 🎉")

    with tab4:
        st.markdown("## 🎴 나만의 포켓몬 카드")
        card_html = f"""
        <div style="
            width: 100%;
            max-width: 520px;
            margin: auto;
            padding: 25px;
            border-radius: 32px;
            background: linear-gradient(135deg, {data["color"]}, #ffffff);
            box-shadow: 0 18px 45px rgba(0,0,0,0.18);
            border: 5px solid white;
            text-align: center;
        ">
            <div style="font-size: 2.5rem;">{data["emoji"]} ✨ 🐾</div>
            <h1 style="color:white; text-shadow:2px 2px 4px rgba(0,0,0,0.25);">
                {safe_name}
            </h1>
            <h2 style="color:#fff;">{mbti} × {data["pokemon"]}</h2>
            <img src="{pokemon_sprite_url(data["id"])}" width="260">
            <div style="
                background: rgba(255,255,255,0.78);
                border-radius: 22px;
                padding: 15px;
                margin-top: 10px;
                font-size: 1.2rem;
                color:#5b4b73;
            ">
                “{data["catch"]}”
                <br><br>
                💞 궁합도 {friendship_score}% · ✨ 반짝임 {sparkle_score}%
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

else:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='glass-box' style='text-align:center;'>
            <h2>🧢 아직 포켓몬 파트너가 소환되지 않았어요!</h2>
            <p>이름과 MBTI를 선택한 뒤 버튼을 눌러보세요. ✨</p>
            <p>귀여운 포켓몬 친구가 등장할지도...? 🐾</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 하단
# =========================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align:center; color:#7d6aa5;'>
        Made with Python, Streamlit, and lots of ✨귀여움✨  
        <br>
        포켓몬 이미지는 PokeAPI sprite를 활용했습니다.
    </div>
    """,
    unsafe_allow_html=True
)
