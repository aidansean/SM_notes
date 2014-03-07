from project_module import project_object, image_object, link_object, challenge_object

p = project_object('SM_notes', 'Standard Model lecture notes')
p.domain = 'http://www.aidansean.com/'
p.path = 'phd_notes'
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.github_repo_name = 'SM_notes'
p.mathjax = False
p.links.append(link_object(p.domain, 'phd_notes/StandardModel.pdf', '[pdf] Compiled notes'))
p.links.append(link_object(p.domain, 'phd_notes/StandardModel.zip', '[zip] Archive'))
p.introduction = 'During my PhD lecture course I typed up my notes as a form of revision.  A few years later someone asked for a copy.  After that I wrote the Feynman diagram maker application and shared the files on a repository.'
p.overview = '''This is a LaTeX project of around 200 pages, so there a lot of LaTeX source files.  In addition there are many images generated with the Feynman diagram maker, as well as many sourced from elsewhere.  These LaTeX source files are shared so that anyone can use them, subject to the terms outlined in the files.'''

p.challenges.append(challenge_object('This project required an extensive collection of figures.', 'Custom Feynman diagram making applciations were developed to produce figures.  Initially PHP and SVG were used to generate some images, but this procedure was found to be too slow.  Instead a Javascript based application was developed that used the HTML canvas, saving images as bitmaps.', 'Resolved'))
