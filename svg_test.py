import cairo
import math


def draw_elliptical_arcs_svg(output_file):
    # SVG surface with width and height
    width, height = 600, 600
    surface = cairo.SVGSurface(output_file, width, height)
    context = cairo.Context(surface)

    # Set line width for the arcs
    context.set_line_width(5)

    # Set arc color
    context.set_source_rgb(1, 0.75, 0.8)  # Pink (RGB: 255, 192, 203)

    # First elliptical arc
    cx, cy = 300, 200  # Center of the ellipse
    radius = 100  # Radius for the circular arc
    start_angle = math.radians(270)  # Start at 45 degrees
    end_angle = math.radians(360)  # End at 135 degrees
    x_scale = 1.0  # Horizontal scaling
    y_scale = 3.0  # Vertical scaling

    # Save the original state before scaling
    context.save()

    # Apply scaling transformation
    context.translate(cx, cy)  # Move to the center of the ellipse
    context.scale(x_scale, y_scale)  # Scale the context
    context.arc(0, 0, radius, start_angle, end_angle)  # Draw arc in scaled space

    # Restore context to undo scaling
    context.restore()

    # Stroke the elliptical arc
    context.stroke()

    # Second elliptical arc
    context.save()
    context.translate(cx, cy)
    context.scale(x_scale, y_scale)
    context.arc(
        0, 0, radius, math.radians(90), math.radians(180)
    )  # Arc in different range
    context.restore()
    context.stroke()

    # Finish the surface
    surface.finish()
    print(f"Saved to {output_file}")


# Example usage
draw_elliptical_arcs_svg("elliptical_arcs.svg")
