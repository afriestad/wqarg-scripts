from get_circles_images import main as get_images
from create_strips import main as create_strips
from downscale_strips import main as downscale_strips
from rank_neighbouring_images import main as rank_neighbouring_images
from find_most_likely_neighbours import main as find_most_likely_neighbours
from build_tjl_link import main as build_tjl_link

if __name__ == "__main__":
    print("=========== Fetching images from web ===========")
    get_images()
    print("========== Creating strips from images =========")
    create_strips()
    print("============== Downscaling strips ==============")
    downscale_strips()
    print("======= Ranking neighbourhood likeliness =======")
    rank_neighbouring_images()
    print("======== Finding most likely neighbours ========")
    find_most_likely_neighbours()
    print("================ Building links ================")
    build_tjl_link()
    print("==================== Done! =====================")