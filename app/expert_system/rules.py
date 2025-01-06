from experta import KnowledgeEngine, Rule, Fact, P


class CocoaDiseaseDetector(KnowledgeEngine):
    # Soil Conditions
    @Rule(Fact(soil_type="not sterilized"))
    def add_organic_matter(self):
        self.declare(Fact(action="Add organic matter like cow dung or peat moss"))

    @Rule(Fact(soil_moisture=P(lambda x: x < 30)))
    def irrigate_plants(self):
        self.declare(Fact(action="Irrigate the plants"))

    @Rule(Fact(soil_moisture=P(lambda x: x > 40)))
    def improve_drainage(self):
        self.declare(Fact(action="Improve drainage"))

    # Temperature and Light
    @Rule(Fact(temperature=P(lambda x: x < 24 or x > 30)))
    def control_temperature(self):
        self.declare(Fact(action="Consider shade or temperature control measures"))

    @Rule(Fact(seedlings_exposed_to_sunlight=True))
    def provide_shade(self):
        self.declare(Fact(action="Provide shade"))

    # Plant Growth Stages
    @Rule(Fact(growth_stage="germination"))
    def germination_stage(self):
        self.declare(Fact(action="Maintain a cool, dry environment"))

    @Rule(Fact(growth_stage="seedling"))
    def seedling_stage(self):
        self.declare(Fact(action="Provide adequate nutrients and water"))

    @Rule(Fact(growth_stage="nursery"))
    def nursery_stage(self):
        self.declare(Fact(action="Harden the seedlings before transplanting"))

    # Pest and Disease Control
    @Rule(Fact(disease="Fusarium wilt"))
    def fusarium_wilt(self):
        self.declare(Fact(action="Use fungicides and improve soil drainage"))

    @Rule(Fact(disease="Phytophthora rot"))
    def phytophthora_rot(self):
        self.declare(Fact(action="Remove infected pods and apply fungicides"))

    @Rule(Fact(disease="Powdery mildew"))
    def powdery_mildew(self):
        self.declare(Fact(action="Apply fungicides and improve air circulation"))

    @Rule(Fact(disease="Leaf spot"))
    def leaf_spot(self):
        self.declare(Fact(action="Remove infected leaves and apply fungicides"))

    @Rule(Fact(disease="Damping-off"))
    def damping_off(self):
        self.declare(Fact(action="Reduce watering and improve drainage"))

    @Rule(Fact(disease="Black pod disease"))
    def black_pod_disease(self):
        self.declare(Fact(action="Remove infected pods and apply fungicides"))

    @Rule(Fact(disease="Ceratocystis canker"))
    def ceratocystis_canker(self):
        self.declare(Fact(action="Prune infected branches and apply fungicides"))
