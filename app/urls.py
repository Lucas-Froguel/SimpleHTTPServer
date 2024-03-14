
from app.router import Router
from app.views import index, echo


router = Router()

router.register("", index)
router.register("echo", echo)

