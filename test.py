#text = 'a:14:{i:0;s:11:"acf/acf.php";i:1;s:67:"color-and-image-swatches-for-variable-product-attributes/plugin.php";i:2;s:50:"contact-form-7-mailchimp-extension/cf7-mch-ext.php";i:3;s:36:"contact-form-7/wp-contact-form-7.php";i:4;s:27:"js_composer/js_composer.php";i:5;s:31:"norebro-extra/norebro-extra.php";i:6;s:39:"norebro-portfolio/norebro-portfolio.php";i:7;s:23:"revslider/revslider.php";i:8;s:41:"wordpress-importer/wordpress-importer.php";i:9;s:24:"wordpress-seo/wp-seo.php";i:10;s:49:"wp-file-download-light/wp-file-download-light.php";i:11;s:35:"wp-smart-editor/wp-smart-editor.php";i:12;s:49:"wp-table-manager-light/wp-table-manager-light.php";i:13;s:33:"wps-hide-login/wps-hide-login.php";}'
def find_plugin_quantity():
    global plug_quantity
    # search for plugin quantity
    plug_pos = text.find("a:") + 2
    end_plug_pos = text.find(":", plug_pos)
    plug_quantity = int(text[plug_pos:end_plug_pos])


text = input("Please enter the plugins text: ")
find_plugin_quantity()
index_input = input("Please enter an index of the plugin: ")
if int(index_input) > (plug_quantity - 1):
    print("Sorry, I can't find the plugin with this number")
    quit()
elif int(index_input) < 0:
    print("Sorry, the plugin number can't be below zero")
    quit()
index = text.find('i:'+ index_input)
if index == -1:
    print("Unfortunately, it is invalid input!")
    quit()
#Find the number near s
s_index = text.find('s:', index)
num_index = text.find(':', s_index+2)
#assign number near s using slice
plugin_position = int(text[s_index+2:num_index])+3
plugin_end = num_index + plugin_position
#plugin from start to end
whole_plugin_slice = text[index:plugin_end+1]
edited_text = text.replace(whole_plugin_slice, '')

#loop to change the indexes
x = int(index_input) + 1
while x < plug_quantity:
    edited_text = edited_text.replace("i:" + str(x), "i:" + str(x-1))
    x += 1
edited_text = edited_text.replace("a:" + str(plug_quantity), "a:" + str(plug_quantity-1))
#print(type(plug_quantity), type(x))
print(edited_text)
#print(plugin_position, plugin_end)
#print(index, s_index, num_index)
#print(whole_plugin_slice)
#print(edited_text)