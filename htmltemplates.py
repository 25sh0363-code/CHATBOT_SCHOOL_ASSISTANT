css = """
<style>
:root {
    --bg: #f7f7f8;
    --panel: #ffffff;
    --line: #e5e7eb;
    --user: #e9f2ff;
    --assistant: #ffffff;
    --text: #111827;
    --muted: #6b7280;
}

.stApp {
    background: radial-gradient(circle at top, #ffffff 0%, var(--bg) 55%);
    color: var(--text);
}

[data-testid="stAppViewContainer"] .main .block-container {
    max-width: 900px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

.chat-message {
    display: flex;
    align-items: flex-start;
    gap: 0.7rem;
    margin: 0.65rem 0;
}

.chat-message.user {
    flex-direction: row-reverse;
}

.chat-message .avatar {
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.72rem;
    flex-shrink: 0;
    border: 1px solid var(--line);
    background: #ffffff;
    color: var(--muted);
}

.chat-message .message {
    max-width: min(80%, 720px);
    border: 1px solid var(--line);
    border-radius: 0.95rem;
    padding: 0.8rem 0.95rem;
    line-height: 1.55;
    color: var(--text);
    background: var(--assistant);
    box-shadow: 0 1px 0 rgba(17, 24, 39, 0.03);
}

.chat-message.user .message {
    background: var(--user);
}

.chat-message p {
    margin: 0;
}

[data-testid="stSidebar"] {
    border-right: 1px solid var(--line);
    background: #fafafa;
}

[data-testid="stTextInputRootElement"] input {
    border-radius: 999px;
    border: 1px solid #d1d5db;
    background: #ffffff;
}
</style>
"""

user_template = """
<div class="chat-message user">
    <div class="avatar">YOU</div>
    <div class="message">{{MSG}}</div>
</div>
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">AI</div>
    <div class="message">{{MSG}}</div>
</div>
"""


