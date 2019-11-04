import subprocess

from selenium import webdriver


def main(trainees_file, samples_directory, output_directory, headless_browser):
    sample_filenames = run_fathom_list(samples_directory)

#   need_to_vectorize = check_for_changes_to_samples_or_ruleset(sample_filenames, trainees_file)
    need_to_vectorize = True
    if not need_to_vectorize:
        vector_file = use_previous_vectors()
    else:
#       fathom_fox, fathom_trainees = build_fathom_addons(trainees_file)
        file_server = set_up_file_server(samples_directory)
        # TODO: Delete this!!!
        fathom_fox = None
        fathom_trainees = None
        firefox = configure_firefox(fathom_fox, fathom_trainees, headless_browser)
#       firefox = set_up_vectorizer(firefox, sample_filenames)
        vector_file, firefox = run_vectorizer(firefox)
        teardown(firefox, file_server)
#   output_vector_file(vector_file, output_directory)


def run_fathom_list(samples_directory):
    result = subprocess.run(['fathom-list', samples_directory, '-r'], capture_output=True)
    sample_filenames = result.stdout.decode().splitlines()
    return sample_filenames


#def check_for_changes_to_samples_or_ruleset(sample_filenames, trainees_file):
#    return need_to_vectorize
#
#
def use_previous_vectors():
    return
#   return vector_file


#def build_fathom_addons(trainees_file):
#    return fathom_fox, fathom_trainees
#
#
def set_up_file_server(samples_directory):
    file_server = subprocess.Popen(['fathom-serve', '-d', samples_directory], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    return file_server


def configure_firefox(fathom_fox, fathom_trainees, headless_browser):
    # TODO: Use a profile with page caching disabled
    options = webdriver.FirefoxOptions()
    options.headless = headless_browser
    firefox = webdriver.Firefox(options=options)
#   profile = webdriver.FirefoxProfile()
#   firefox.install_addon('C:/Users/Daniel/code/fathom-fox/fathom-fox.xpi')
    return firefox


#def set_up_vectorizer(firefox, sample_filenames):
#    return firefox
#
#
def run_vectorizer(firefox):
    # TODO: Make this do real stuff!!!
    firefox.get('https://www.mozilla.org/en-US/')
    # TODO: Delete this!!!
    vector_file = None
    return vector_file, firefox


def teardown(firefox, file_server):
    # TODO: This doesn't actually stop fathom-serve from running on my machine???
    file_server.terminate()
    file_server.kill()
    file_server.wait()
    firefox.quit()


#def output_vector_file(vector_file, output_directory):
#    pass


if __name__ == '__main__':
    # TODO: Real CLI arguments
    main(
        trainees_file=None,
        samples_directory='C:/Users/Daniel/code/fathom-smoot/shopping/samples/training',
        output_directory=None,
        headless_browser=False,
    )
