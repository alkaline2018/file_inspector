from file_inspector import FileInspector

# 분석 대상 파일 경로 (예시)
file_path = "./sample.csv"

# 인스턴스 생성 및 분석 수행
inspector = FileInspector()
result = inspector.inspect(file_path)

# Slack 형식 메시지 출력
print("📣 Slack Message Format:\n")
from file_inspector.formatter.slack_formatter import format_slack_message
print(format_slack_message(result.file_info, result.df))

# Markdown 출력 (예: Notion 복붙용)
print("\n📝 Markdown Format:\n")
from file_inspector.formatter.markdown_formatter import format_markdown_report
print(format_markdown_report(result.file_info, result.df))

# HTML 출력 (예: 리포트용)
print("\n🌐 HTML Format:\n")
from file_inspector.formatter.html_formatter import format_html_report
print(format_html_report(result.file_info, result.df))

# JSON 출력 (예: API 응답용)
print("\n📦 JSON Format:\n")
from file_inspector.formatter.json_formatter import format_json_report
print(format_json_report(result.file_info, result.df))
