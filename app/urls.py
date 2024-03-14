
from app.router import Router
from app.views import index, echo, user_agent


router = Router()

router.register("", index)
router.register("echo", echo)
router.register("user-agent", user_agent)

