
from app.router import Router
from app.views import index, echo, user_agent, files


router = Router()

router.register("", index)
router.register("echo", echo)
router.register("user-agent", user_agent)
router.register("files", files)

