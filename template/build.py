from bump import SemVer
from pyorigins.archive import Archive
from pyorigins.badge import Badge
from pyorigins.origin import Origin
from pyorigins.origin_layer import OriginLayer
from pyorigins.origin_pack import OriginPack
from pyorigins.pack_meta import PackMeta
from pyorigins.power import ChargePower, Power, EdiblePower
from pyorigins.resource import Component, ActionOverTime
from pyorigins.stage_factory import StageFactory
from pyorigins.stage import Stage
from pyorigins.tag import Tag
from .setup import Setup
import os

def build():
  setup = Setup()
  semver = SemVer.parse(setup.version)
  current_path = os.path.dirname(__file__)
  archive_path = os.path.join(current_path, "archive")
  src_path = os.path.join(current_path, "build")

  meta = PackMeta(
    15,
    " ".join([
      setup.desc, "v" + setup.version, "by", setup.author])
  )

  credits = Power(
    "Credits",
    "; ".join([
      "Version: " + setup.version,
      "Author: " + setup.author,
    ]),
    "origins:simple"
  )

  origin = Origin(
    setup.namespace,
    "",
    "",
  ).with_order(0).with_impact(2).with_icon(
    ""
  ).add_powers([
    credits,
  ])

  origin_layer = OriginLayer(
    [
      origin,
    ]
  ).with_data(
    {
      "replace": False,
    }
  )

  archive = Archive(
    "zip",
    "_".join([setup.name, "v" + setup.version]),
    os.path.join(archive_path, "v" + ".".join([str(semver.major), str(semver.minor)])),
    src_path
  )

  OriginPack(
    src_path,
    setup.namespace,
  ).with_meta(
    meta
  ).with_origins(
    [
      origin,
    ]
  ).with_origin_layers(
    [
      origin_layer,
    ]
  ).with_powers(
    [
      credits,
    ]
  ).with_tags(
    [
    ]
  ).with_archive(
    archive
  ).build()

if __name__ == "__main__":
  build()
