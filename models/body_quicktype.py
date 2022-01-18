# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = video_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AroundPlanet:
    planet: str
    rel: str

    @staticmethod
    def from_dict(obj: Any) -> 'AroundPlanet':
        assert isinstance(obj, dict)
        planet = from_str(obj.get("planet"))
        rel = from_str(obj.get("rel"))
        return AroundPlanet(planet, rel)

    def to_dict(self) -> dict:
        result: dict = {}
        result["planet"] = from_str(self.planet)
        result["rel"] = from_str(self.rel)
        return result


class BodyType(Enum):
    ASTEROID = "Asteroid"
    BODY_TYPE_MOON = "moon"
    COMET = "Comet"
    DWARF_PLANET = "Dwarf Planet"
    MOON = "Moon"
    PLANET = "Planet"
    STAR = "Star"


@dataclass
class Mass:
    mass_value: float
    mass_exponent: int

    @staticmethod
    def from_dict(obj: Any) -> 'Mass':
        assert isinstance(obj, dict)
        mass_value = from_float(obj.get("massValue"))
        mass_exponent = from_int(obj.get("massExponent"))
        return Mass(mass_value, mass_exponent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["massValue"] = to_float(self.mass_value)
        result["massExponent"] = from_int(self.mass_exponent)
        return result


@dataclass
class Moon:
    moon: str
    rel: str

    @staticmethod
    def from_dict(obj: Any) -> 'Moon':
        assert isinstance(obj, dict)
        moon = from_str(obj.get("moon"))
        rel = from_str(obj.get("rel"))
        return Moon(moon, rel)

    def to_dict(self) -> dict:
        result: dict = {}
        result["moon"] = from_str(self.moon)
        result["rel"] = from_str(self.rel)
        return result


@dataclass
class Vol:
    vol_value: float
    vol_exponent: int

    @staticmethod
    def from_dict(obj: Any) -> 'Vol':
        assert isinstance(obj, dict)
        vol_value = from_float(obj.get("volValue"))
        vol_exponent = from_int(obj.get("volExponent"))
        return Vol(vol_value, vol_exponent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["volValue"] = to_float(self.vol_value)
        result["volExponent"] = from_int(self.vol_exponent)
        return result


@dataclass
class Body:
    id: str
    name: str
    english_name: str
    is_planet: bool
    semimajor_axis: int
    perihelion: int
    aphelion: int
    eccentricity: float
    inclination: float
    density: float
    gravity: float
    escape: float
    mean_radius: float
    equa_radius: float
    polar_radius: float
    flattening: float
    dimension: str
    sideral_orbit: float
    sideral_rotation: float
    discovered_by: str
    discovery_date: str
    alternative_name: str
    axial_tilt: float
    avg_temp: int
    main_anomaly: float
    arg_periapsis: float
    long_asc_node: float
    body_type: BodyType
    rel: str
    moons: Optional[List[Moon]] = None
    mass: Optional[Mass] = None
    vol: Optional[Vol] = None
    around_planet: Optional[AroundPlanet] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Body':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        english_name = from_str(obj.get("englishName"))
        is_planet = from_bool(obj.get("isPlanet"))
        semimajor_axis = from_int(obj.get("semimajorAxis"))
        perihelion = from_int(obj.get("perihelion"))
        aphelion = from_int(obj.get("aphelion"))
        eccentricity = from_float(obj.get("eccentricity"))
        inclination = from_float(obj.get("inclination"))
        density = from_float(obj.get("density"))
        gravity = from_float(obj.get("gravity"))
        escape = from_float(obj.get("escape"))
        mean_radius = from_float(obj.get("meanRadius"))
        equa_radius = from_float(obj.get("equaRadius"))
        polar_radius = from_float(obj.get("polarRadius"))
        flattening = from_float(obj.get("flattening"))
        dimension = from_str(obj.get("dimension"))
        sideral_orbit = from_float(obj.get("sideralOrbit"))
        sideral_rotation = from_float(obj.get("sideralRotation"))
        discovered_by = from_str(obj.get("discoveredBy"))
        discovery_date = from_str(obj.get("discoveryDate"))
        alternative_name = from_str(obj.get("alternativeName"))
        axial_tilt = from_float(obj.get("axialTilt"))
        avg_temp = from_int(obj.get("avgTemp"))
        main_anomaly = from_float(obj.get("mainAnomaly"))
        arg_periapsis = from_float(obj.get("argPeriapsis"))
        long_asc_node = from_float(obj.get("longAscNode"))
        body_type = BodyType(obj.get("bodyType"))
        rel = from_str(obj.get("rel"))
        moons = from_union([from_none, lambda x: from_list(Moon.from_dict, x)], obj.get("moons"))
        mass = from_union([Mass.from_dict, from_none], obj.get("mass"))
        vol = from_union([Vol.from_dict, from_none], obj.get("vol"))
        around_planet = from_union([AroundPlanet.from_dict, from_none], obj.get("aroundPlanet"))
        return Body(id, name, english_name, is_planet, semimajor_axis, perihelion, aphelion, eccentricity, inclination, density, gravity, escape, mean_radius, equa_radius, polar_radius, flattening, dimension, sideral_orbit, sideral_rotation, discovered_by, discovery_date, alternative_name, axial_tilt, avg_temp, main_anomaly, arg_periapsis, long_asc_node, body_type, rel, moons, mass, vol, around_planet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        result["englishName"] = from_str(self.english_name)
        result["isPlanet"] = from_bool(self.is_planet)
        result["semimajorAxis"] = from_int(self.semimajor_axis)
        result["perihelion"] = from_int(self.perihelion)
        result["aphelion"] = from_int(self.aphelion)
        result["eccentricity"] = to_float(self.eccentricity)
        result["inclination"] = to_float(self.inclination)
        result["density"] = to_float(self.density)
        result["gravity"] = to_float(self.gravity)
        result["escape"] = to_float(self.escape)
        result["meanRadius"] = to_float(self.mean_radius)
        result["equaRadius"] = to_float(self.equa_radius)
        result["polarRadius"] = to_float(self.polar_radius)
        result["flattening"] = to_float(self.flattening)
        result["dimension"] = from_str(self.dimension)
        result["sideralOrbit"] = to_float(self.sideral_orbit)
        result["sideralRotation"] = to_float(self.sideral_rotation)
        result["discoveredBy"] = from_str(self.discovered_by)
        result["discoveryDate"] = from_str(self.discovery_date)
        result["alternativeName"] = from_str(self.alternative_name)
        result["axialTilt"] = to_float(self.axial_tilt)
        result["avgTemp"] = from_int(self.avg_temp)
        result["mainAnomaly"] = to_float(self.main_anomaly)
        result["argPeriapsis"] = to_float(self.arg_periapsis)
        result["longAscNode"] = to_float(self.long_asc_node)
        result["bodyType"] = to_enum(BodyType, self.body_type)
        result["rel"] = from_str(self.rel)
        result["moons"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Moon, x), x)], self.moons)
        result["mass"] = from_union([lambda x: to_class(Mass, x), from_none], self.mass)
        result["vol"] = from_union([lambda x: to_class(Vol, x), from_none], self.vol)
        result["aroundPlanet"] = from_union([lambda x: to_class(AroundPlanet, x), from_none], self.around_planet)
        return result


@dataclass
class Video:
    bodies: List[Body]

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        bodies = from_list(Body.from_dict, obj.get("bodies"))
        return Video(bodies)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bodies"] = from_list(lambda x: to_class(Body, x), self.bodies)
        return result


def video_from_dict(s: Any) -> Video:
    return Video.from_dict(s)


def video_to_dict(x: Video) -> Any:
    return to_class(Video, x)
