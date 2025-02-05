import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)


TOKEN = 'YOUR_BOT_TOKEN'


jokes = [
    "Почему программисты не могут играть в футбол? Потому что они не могут найти поле.",
    "Какой язык программирования предпочитает пират? R!",
    "Почему компьютер не может есть обед? Потому что он всегда зависает!",
    "Какой язык программирования предпочитают невесты? Java! Потому что они всегда хотят быть объектами.",
    "Почему программисты всегда путают Рождество и Хэллоуин? Потому что Oct 31 == Dec 25.",
    "Какой язык программирования лучше всего подходит для поиска бага? Ловкач.",
    "Какой напиток предпочитают программисты? Кофе, потому что Java в чистом виде.",
    "Почему программисты не могут бегать? Потому что они всегда находятся в одном месте — в цикле.",
    "Почему программисты не выходят на улицу? Потому что они боятся ошибок.",
    "Почему программисты не идут на свидания? Потому что они не могут найти 'правильное выражение'.",
    "Почему программисты любят машины? Потому что они могут контролировать свои «параметры».",
    "Какой язык программирования любят программисты-пираты? Р-уби!",
    "Почему программисты предпочитают темные темы? Потому что они могут больше сосредоточиться на коде.",
    "Что сказал программист, когда увидел жену? Это выглядит как красивая функция!",
    "Почему программисты не могут найти свою любовь? Потому что их алгоритмы слишком сложны.",
    "Какой способ отладки лучше всего? Отладка в пижаме.",
    "Почему программисты не могут кататься на скейтборде? Потому что их код всегда делает их неустойчивыми.",
    "Какой язык программирования лучше всего подходит для семейных отношений? Python, потому что он поддерживает наследование.",
    "Почему программисты не могут пить чай? Потому что они не могут найти правильный тип.",
    "Что программисты говорят, когда не могут найти ошибку? 'Где же это... ерунда?'",
    "Почему программисты любят небо? Потому что это идеальная среда для тестирования их кода.",
    "Какой язык программирования лучше всего для команды? JavaScript, потому что он помогает работать с клиентом.",
    "Какой код никогда не выходит из моды? Код, который хорошо написан.",
    "Почему программисты никогда не опаздывают? Потому что они всегда синхронизированы.",
    "Какой язык программирования используется для хранения секретов? SQL, потому что он знает, как держать все в секрете.",
    "Почему программисты не могут плавать? Потому что они всегда боятся утонуть в своих ошибках.",
    "Какой язык программирования лучше всего для командной работы? C#, потому что он всегда рядом.",
    "Что делает программист, когда чувствует себя плохо? Он обновляет свои библиотеки.",
    "Почему программисты не могут найти работу? Потому что их коды всегда на проверке.",
    "Какой язык программирования лучше всего для экстренных случаев? C++, потому что он может справиться с любой ситуацией.",
    "Почему программисты не любят шоколад? Потому что он может привести к проблемам с конфигурацией.",
    "Какой язык программирования лучше всего для веб-дизайна? HTML, потому что он всегда поддерживает структуру.",
    "Почему программисты не могут найти своего друга? Потому что он всегда в отладочном режиме.",
    "Какой язык программирования подходит для работы в офисе? Python, потому что он легко интегрируется.",
    "Почему программисты любят кофе? Потому что это их лучшая функция.",
    "Какой язык программирования лучше всего для путешествий? Java, потому что он всегда в пути.",
    "Почему программисты не могут путешествовать по миру? Потому что они всегда в разработке.",
    "Какой язык программирования лучше всего для романтики? Ruby, потому что он всегда о любви.",
    "Почему программисты не могут спать? Потому что их код всегда работает.",
    "Какой язык программирования лучше всего для музыки? Swift, потому что он всегда в ритме.",
    "Почему программисты не могут сесть на диету? Потому что они всегда зависят от своих данных.",
    "Какой язык программирования лучше всего для путешествий по времени? JavaScript, потому что он всегда в будущем.",
    "Почему программисты не могут найти счастье? Потому что их алгоритмы всегда слишком сложны.",
    "Какой язык программирования лучше всего для кулинарии? PHP, потому что он может добавить много вкуса.",
    "Почему программисты не могут кататься на роликах? Потому что их код всегда на грани поломки.",
    "Какой язык программирования лучше всего для физических упражнений? Ruby, потому что он всегда в форме.",
    "Почему программисты не могут работать в парке? Потому что они не могут найти нужный алгоритм.",
    "Какой язык программирования лучше всего для рисования? HTML, потому что он может создать любой рисунок.",
    "Почему программисты не могут быть хорошими друзьями? Потому что они всегда слишком заняты кодированием.",
    "Какой язык программирования лучше всего для подводного плавания? C++, потому что он может работать под водой.",
    "Почему программисты не могут быть на пляже? Потому что их код не терпит песка.",
    "Какой язык программирования лучше всего для сна? Python, потому что он всегда расслабляет.",
    "Почему программисты не могут быть врачами? Потому что их код всегда требует отладки.",
    "Какой язык программирования лучше всего для воспитания детей? Java, потому что он поддерживает наследование.",
    "Почему программисты не могут быть актерами? Потому что их код всегда требует сценария.",
    "Какой язык программирования лучше всего для общения? JavaScript, потому что он всегда на связи.",
    "Почему программисты не могут быть шахматистами? Потому что их код всегда слишком сложен для игры.",
    "Какой язык программирования лучше всего для экстрима? C++, потому что он всегда на грани.",
    "Почему программисты не могут быть художниками? Потому что их код всегда слишком геометричен.",
    "Какой язык программирования лучше всего для рекламы? HTML, потому что он всегда привлекает внимание.",
    "Почему программисты не могут быть поварами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для путешествий по космосу? JavaScript, потому что он может достичь любой планеты.",
    "Почему программисты не могут быть парикмахерами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для общения с животными? Python, потому что он дружелюбен.",
    "Почему программисты не могут быть профессиональными спортсменами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для проведения праздников? PHP, потому что он может сделать любое событие особенным.",
    "Почему программисты не могут быть водителями? Потому что их код всегда требует корректировки.",
    "Какой язык программирования лучше всего для написания книг? Java, потому что он всегда поддерживает структуру.",
    "Почему программисты не могут быть финансистами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с природой? C++, потому что он может справиться с любыми условиями.",
    "Почему программисты не могут быть дирижерами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с датами? Python, потому что он может обработать любое время.",
    "Почему программисты не могут быть путешественниками? Потому что их код всегда требует времени.",
    "Какой язык программирования лучше всего для написания музыки? Swift, потому что он всегда в ритме.",
    "Почему программисты не могут быть поварами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с графикой? JavaScript, потому что он может создать любой рисунок.",
    "Почему программисты не могут быть архитекторами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с текстом? Ruby, потому что он может создать любой текст.",
    "Почему программисты не могут быть актерами? Потому что их код всегда требует сценария.",
    "Какой язык программирования лучше всего для работы с цветами? HTML, потому что он может создать любой цвет.",
    "Почему программисты не могут быть биологами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для создания игр? C++, потому что он может справиться с любой задачей.",
    "Почему программисты не могут быть психотерапевтами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с интернетом? JavaScript, потому что он всегда на связи.",
    "Почему программисты не могут быть путешественниками? Потому что их код всегда требует времени.",
    "Какой язык программирования лучше всего для работы с аудио? Python, потому что он может обработать любой звук.",
    "Почему программисты не могут быть военными? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с видео? JavaScript, потому что он может создать любое видео.",
    "Почему программисты не могут быть юристами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с 3D-графикой? C++, потому что он может создать любой объем.",
    "Почему программисты не могут быть художниками? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с виртуальной реальностью? Java, потому что он может создать любой мир.",
    "Почему программисты не могут быть архитекторами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с роботами? Python, потому что он дружелюбен.",
    "Почему программисты не могут быть моделями? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с данными? SQL, потому что он может хранить любую информацию.",
    "Почему программисты не могут быть биологами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с большими данными? Hadoop, потому что он может справиться с любыми объемами.",
    "Почему программисты не могут быть дирижерами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с безопасностью? Python, потому что он может защитить любую информацию.",
    "Почему программисты не могут быть архитекторами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с системами? Java, потому что он всегда поддерживает структуру.",
    "Почему программисты не могут быть педагогами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с облаками? AWS, потому что он может создать любое облако.",
    "Почему программисты не могут быть художниками? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с устройствами? C++, потому что он может работать с любым оборудованием.",
    "Почему программисты не могут быть военными? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с сетями? Python, потому что он может создать любую сеть.",
    "Почему программисты не могут быть полицейскими? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с машинным обучением? TensorFlow, потому что он может обучить любую модель.",
    "Почему программисты не могут быть врачами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с вычислениями? Python, потому что он может справиться с любыми расчетами.",
    "Почему программисты не могут быть ветеринарами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с текстом? Ruby, потому что он может создать любой текст.",
    "Почему программисты не могут быть музыкантами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с сетью? JavaScript, потому что он всегда на связи.",
    "Почему программисты не могут быть художниками? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с криптографией? Python, потому что он может защитить любую информацию.",
    "Почему программисты не могут быть архитекторами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с данными? SQL, потому что он может хранить любую информацию.",
    "Почему программисты не могут быть учеными? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с веб-разработкой? JavaScript, потому что он может создать любой сайт.",
    "Почему программисты не могут быть актерами? Потому что их код всегда требует сценария.",
    "Какой язык программирования лучше всего для работы с системами? Java, потому что он всегда поддерживает структуру.",
    "Почему программисты не могут быть политиками? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с API? Python, потому что он может интегрировать любые системы.",
    "Почему программисты не могут быть психологами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с большими данными? Hadoop, потому что он может справиться с любыми объемами.",
    "Почему программисты не могут быть путешественниками? Потому что их код всегда требует времени.",
    "Какой язык программирования лучше всего для работы с облачными технологиями? AWS, потому что он может создать любое облако.",
    "Почему программисты не могут быть педагогами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с роботами? Python, потому что он дружелюбен.",
    "Почему программисты не могут быть дирижерами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с графикой? JavaScript, потому что он может создать любой рисунок.",
    "Почему программисты не могут быть художниками? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с виртуальной реальностью? Java, потому что он может создать любой мир.",
    "Почему программисты не могут быть архитекторами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с данными? SQL, потому что он может хранить любую информацию.",
    "Почему программисты не могут быть бухгалтерами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с системами? Java, потому что он всегда поддерживает структуру.",
    "Почему программисты не могут быть поварами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с машинами? C++, потому что он может справиться с любыми задачами.",
    "Почему программисты не могут быть дирижерами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с сетями? Python, потому что он может создать любую сеть.",
    "Почему программисты не могут быть актерами? Потому что их код всегда требует сценария.",
    "Какой язык программирования лучше всего для работы с аудио? JavaScript, потому что он может создать любой звук.",
    "Почему программисты не могут быть полицейскими? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с видео? Python, потому что он может обработать любое видео.",
    "Почему программисты не могут быть учеными? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с текстом? Ruby, потому что он может создать любой текст.",
    "Почему программисты не могут быть музыкантами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с графикой? JavaScript, потому что он может создать любые изображения.",
    "Почему программисты не могут быть ветеринарами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с системами? Java, потому что он всегда поддерживает структуру.",
    "Почему программисты не могут быть врачами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с данными? SQL, потому что он может хранить любую информацию.",
    "Почему программисты не могут быть юристами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с интернетом? JavaScript, потому что он может создать любой сайт.",
    "Почему программисты не могут быть педагогами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с криптографией? Python, потому что он может защитить любую информацию.",
    "Почему программисты не могут быть художниками? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с роботами? Python, потому что он дружелюбен.",
    "Почему программисты не могут быть дизайнерами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с графикой? JavaScript, потому что он может создать любые изображения.",
    "Почему программисты не могут быть актерами? Потому что их код всегда требует сценария.",
    "Какой язык программирования лучше всего для работы с виртуальной реальностью? Java, потому что он может создать любой мир.",
    "Почему программисты не могут быть архитекторами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с текстом? Ruby, потому что он может создать любой текст.",
    "Почему программисты не могут быть поварами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с сетями? Python, потому что он может создать любую сеть.",
    "Почему программисты не могут быть дирижерами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с аудио? JavaScript, потому что он может создать любой звук.",
    "Почему программисты не могут быть полицейскими? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с видео? Python, потому что он может обработать любое видео.",
    "Почему программисты не могут быть ветеринарами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с системами? Java, потому что он всегда поддерживает структуру.",
    "Почему программисты не могут быть врачами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с данными? SQL, потому что он может хранить любую информацию.",
    "Почему программисты не могут быть юристами? Потому что их код всегда требует точности.",
    "Какой язык программирования лучше всего для работы с интернетом? JavaScript, потому что он может создать любой сайт.",
    "Почему программисты не могут быть педагогами? Потому что их код всегда требует внимания.",
    "Какой язык программирования лучше всего для работы с криптографией? Python, потому что он может защитить любую информацию.",
]


@bot.event
async def on_message(message):
  
    if message.author == bot.user:
        return

   
    response = random.choice(jokes)
    await message.channel.send(response)

  
    await bot.process_commands(message)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


bot.run(TOKEN)
