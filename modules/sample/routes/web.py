from ...sample import sample
from ..controllers.SampleController import SampleController

route = sample.route
SampleController = SampleController()

route.get("/sample", SampleController.sample)