% scale(1000) import("roller.stl");

// Append pure shapes (cube, cylinder and sphere), e.g:
// cube([10, 10, 10], center=true);
// cylinder(r=10, h=10, center=true);
translate([0,0,0])
sphere(15.5);

translate([0,0,8.5])
sphere(15.5);

translate([0,0,-8.5])
sphere(15.5);

translate([0,0,16.5])
sphere(15);

translate([0,0,-16.5])
sphere(15);

translate([0,0,23.5])
sphere(14);

translate([0,0,-23.5])
sphere(14);