"""Setup the AI and its goals"""
from colorama import Fore, Style
from autogpt import utils
from autogpt.config.ai_config import AIConfig
from autogpt.logs import logger


def prompt_user() -> AIConfig:
    """Prompt the user for input

    Returns:
        AIConfig: The AIConfig object containing the user's input
    """
    ai_name = ""
    # Construct the prompt
    logger.typewriter_log(
        "欢迎来到 Auto-GPT-ZH! 中文版由weick提供. ",
        Fore.GREEN,
        "",
        speak_text=True,
    )
    logger.typewriter_log(
        "加入社区一起玩转AI.",
        Fore.YELLOW,
        "",
        speak_text=True,
    )

    print("在下面输入您的 AI 的名称及其角色。不输入将使用默认名称")
    # Get AI Name from User
    logger.typewriter_log(
         "为您的 AI 命名：",Fore.GREEN,"例如，'chaos-1号'"
     )
    ai_name = utils.clean_input("AI 机器人名称: ")
    if ai_name == "":
        ai_name = "chaos-1号"

    logger.typewriter_log(
        f"{ai_name} 在这里!", Fore.LIGHTBLUE_EX, "我随时为您服务。", speak_text=True
    )

    # Get AI Role from User
    logger.typewriter_log(
        "描述您的 AI 的职责：",
        Fore.GREEN,
        "例如，'一种协助编程的人工智能，协助进行python语言django开发。"
    )
    ai_role = utils.clean_input(f"{ai_name} 的职责: ")
    if ai_role == "":
        ai_role = "一种协助进行python语言django开发的人工智能。"

    # Enter up to 5 goals for the AI
    logger.typewriter_log(
        "提示:输入最多5个要帮你实现的功能/目标 ",
        Fore.GREEN,
         "例如：\n使用django DRF开发任务管理系统、创建学生管理系统的django模型等等")
    print("输入空白以加载默认值，完成时不要输入任何内容。", flush=True)
    ai_goals = []
    for i in range(5):
        ai_goal = utils.clean_input(f"{Fore.LIGHTBLUE_EX}Goal{Style.RESET_ALL} {i+1}: ")
        if ai_goal == "":
            break
        ai_goals.append(ai_goal)
    if len(ai_goals) == 0:
        ai_goals = [
            "Increase net worth",
            "Grow Twitter Account",
            "Develop and manage multiple businesses autonomously",
        ]

    return AIConfig(ai_name, ai_role, ai_goals)
