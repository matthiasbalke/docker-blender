FROM centos:centos7

LABEL maintainer "matthias.balke@googlemail.com"

WORKDIR /opt
ADD setup_slave.py setup_slave.py

RUN yum update -y && \
    yum install -y curl bzip2 freetype mesa-libGLU libXi libXrender

RUN curl -O http://ftp.halifax.rwth-aachen.de/blender/release/Blender2.78/blender-2.78c-linux-glibc219-x86_64.tar.bz2
RUN tar xjf blender-*.tar.bz2
RUN mv blender-*x86_64 blender
RUN rm -f blender-*.tar.bz2

RUN mkdir -p /tmp/blender-output

#/opt/blender/blender --background -a -noaudio -nojoystick -E CYCLES --render-output /tmp/blender-output/render --python /opt/setup_slave.py
# blender -b file.blend -E CYCLES -t 0 --render-output /tmp/blender-output -P script.py
