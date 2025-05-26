import argparse
import os
from onshape_to_robot.message import bright, error, info

arg_parser = argparse.ArgumentParser(description="Test loading a model")
arg_parser.add_argument(
    "model_name",
    type=str,
    help="The example to test loading (e.g., '2wheels_urdf', '2wheels_mujoco', etc.)",
)
args = arg_parser.parse_args()

if "urdf" in args.model_name:
    import pinocchio

    print(info("Loading model in pinocchio"))
    output_filename = f"{args.model_name}/robot.urdf"
    model = pinocchio.buildModelFromUrdf(output_filename)
    pinocchio.buildGeomFromUrdf(
        model,
        output_filename,
        pinocchio.COLLISION,
        package_dirs=os.path.dirname(output_filename),
    )
    pinocchio.buildGeomFromUrdf(
        model,
        output_filename,
        pinocchio.VISUAL,
        package_dirs=os.path.dirname(output_filename),
    )
elif "mujoco" in args.model_name:
    import mujoco

    print(info("Loading model in mujoco"))
    output_filename = f"{args.model_name}/scene.xml"
    mujoco.MjModel.from_xml_path(output_filename)
