project(RORPO2D)
cmake_minimum_required(VERSION 2.8)
set(CMAKE_CXX_FLAGS "-std=c++98")

# Add files
file( GLOB_RECURSE HEADER_FILES *.h *.hpp)
file( GLOB_RECURSE SOURCE_FILES *.c *.cpp )

# Find libpng library
find_package(PNG REQUIRED)
include_directories(${PNG_INCLUDE_DIR})

# Create executable and link library
add_executable(${PROJECT_NAME} ${SOURCE_FILES} ${HEADER_FILES})
target_link_libraries(${PROJECT_NAME} ${PNG_LIBRARY})

######## CMAKE UTILISE POUR NOS TESTS ######
#### Nous avons du apporter des modifications pour prendre en comte des erreurs de versions et chemins d'accès.
# project(RORPO2D)
# cmake_minimum_required(VERSION 2.8)
# set(CMAKE_CXX_FLAGS "-std=c++98")



# # Add files
# file( GLOB_RECURSE HEADER_FILES *.h *.hpp)
# file( GLOB_RECURSE SOURCE_FILES *.c *.cpp )


# # Find libpng library

# find_package(PkgConfig REQUIRED)
# pkg_check_modules(PNG libpng16 REQUIRED)

# include_directories(${PNG_INCLUDE_DIRS})
# link_directories(${PNG_LIBRARY_DIRS})
# link_libraries(${PNG_LIBRARIES})

# # Create executable and link library
# add_executable(${PROJECT_NAME} ${SOURCE_FILES} ${HEADER_FILES})
# target_link_libraries(${PROJECT_NAME} ${PNG_LIBRARY})


