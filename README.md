<p>Here is a little script that renders characters to 2d images the way it was done in Diablo 2. So the
    one will be able to use the images in 2d engines (like GameMaker).</p>
<p>Images combined in game engine:<img data-fr-image-pasted="true" src="https://s3.amazonaws.com/markets-rails/uploads%2F1534261224175-test2.gif"
    class="fr-fic fr-dii"></p>
<p>The images themselves:<img data-fr-image-pasted="true" src="https://s3.amazonaws.com/markets-rails/uploads%2F1534261752250-test3.gif"
    class="fr-fic fr-dii">
    <br>
</p>
<p>
    <br>
</p>
<p><strong><span style="font-size: 18px;">What add-on can do:</span></strong></p>
<ol>
    <li>Render all the actions (fake ones) of .blend file;</li>
    <li>Render only specified actions chosen by user (fake ones);</li>
    <li>Render specified number of directions;</li>
    <li>Render all the render layers or only render layers chosen by user;</li>
    <li>Set output path for rendered images.</li>
</ol>
<p>
    <br>
</p>
<p><strong><span style="font-size: 18px;">How to use the add-on:</span></strong></p>
<ul>
    <li>Install the add-on: <strong>File &gt; User Preferences &gt; Install add-on from File... &gt; Select downloaded add-on &gt; Activate it</strong></li>
    <li>Create <strong>Empty&nbsp;</strong>named <em>Empty&nbsp;</em>and parent your rig to it;</li>
    <li>Open the <strong>Toolshelf (T)&nbsp;</strong>and scroll down to <strong>Character Renderer</strong>        tab:</li>
    <li><img src="https://s3.amazonaws.com/markets-rails/uploads%2F1534270848687-toolshelf2.png" style="width: 300px;"
        class="fr-fic fr-dib fr-fil"></li>
    <li><strong>Save Path:&nbsp;</strong>set here the folder where all the animations will be rendered;</li>
    <li><strong>Rig Name:&nbsp;</strong>set here your character's rig name;</li>
    <li><strong>Camera Angles:&nbsp;</strong>number of angles. For example: 8 angles mean default angles
        for isometric game (i.e. 0, 45, 90, 135, 180, 225, 270, 315 degrees);</li>
    <li><strong>Fake All Actions:&nbsp;</strong>make all the actions in .blend file Fake. All actions will
        be rendered with <em>Render Fake Actions</em> button. Add-on renders only Fake actions (marked
        with <strong>F&nbsp;</strong>in drop-down menu in actions' list). Make Fake actions only the
        ones you want to render. <em>Fake All Actions</em> button is actually just for the convenience
        - not to make all actions Fake by hand. <strong>IMPORTANT NOTE:&nbsp;</strong><u>never close your file with actions that are not Fake. It may delete them completely from the project even if the project is saved.&nbsp;</u>
        <img
        src="https://s3.amazonaws.com/markets-rails/uploads%2F1534270501964-fake.png" style="width: 243px;"
        class="fr-fic fr-dib fr-fil"></li>
    <li><strong>Unfake All Actions:&nbsp;</strong>make all the actions in .blend file unfake. No actions
        will be rendered with <em>Render Fake Actions</em> button.</li>
    <li><strong>Enable All Render Layers:&nbsp;</strong>enable all the Render Layers what means that all
        the parts of the character will be rendered.<strong>&nbsp;</strong>Few words about how one should
        organize parts of the character to render them separately. Rendering different parts of character
        achieved by:&nbsp;
        <ol>
            <li>Placing that parts to different <em>visible</em> layers:<span class="fr-img-caption fr-fic fr-dib fr-fil"
                style="width: 300px; width: 300px;"><span class="fr-img-wrap"><img src="https://s3.amazonaws.com/markets-rails/uploads%2F1534271777878-layers.gif"><span class="fr-inner">Each part is on it's own visible layer</span></span>
                </span>
            </li>
            <li>Adding corresponding (each visible layer = corresponding render layer) <em>Render Layers:<span class="fr-img-caption fr-fic fr-dib fr-fil" style="width: 300px; width: 300px;"><span class="fr-img-wrap"><img src="https://s3.amazonaws.com/markets-rails/uploads%2F1534272438217-renderLayers2.gif"><span class="fr-inner">In this case all the Render Layers except the <em>Preview will be rendered</em></span>
                </span>
                </span>
                </em>
            </li>
            <li>Only selected Render Layers will be rendered with the <em>Render Fake Actions&nbsp;</em>button.</li>
        </ol>
    </li>
    <li><strong>Disable All Render Layers:&nbsp;</strong>disable all the Render Layers what means that no
        parts of the character will be rendered. <em>Disable All Render Layers</em> button is actually
        just for the convenience - not to disable all the render layers by hand.</li>
    <li><strong>Render Fake Actions:&nbsp;</strong>render all the parts of character defined by Render Layers
        from all Fake actions to specified output path.<span class="fr-img-caption fr-fic fr-dib fr-draggable"
        contenteditable="false" draggable="false" style="width: 300px; width: 300px; width: 300px;"><span class="fr-img-wrap"><span class="fr-inner" contenteditable="true"></span></span>
        </span>
    </li>
</ul>
<p><strong><span style="font-size: 18px;">Credits:</span></strong></p>
<p>Add-on based on <em>Tamir Lousky</em> aka <em>TLousky&nbsp;</em>answer on <a href="https://blender.stackexchange.com/a/73699"
    rel="noopener noreferrer" target="_blank">blender.stackexchange</a>
    <a href="https://blender.stackexchange.com/a/73699"
    rel="noopener noreferrer" target="_blank"></a><a href="https://blender.stackexchange.com/a/73699" rel="noopener noreferrer" target="_blank">&nbsp;</a></p>
<p>For purposes of demonstation some free 3d-models used:</p>
<p><a href="https://www.blendswap.com/blends/view/83828">https://www.blendswap.com/blends/view/83828</a></p>
<p><a href="https://www.blendswap.com/blends/view/88425">https://www.blendswap.com/blends/view/88425</a></p>
<p>
    <br>
</p>
<p>You also can download this add-on absolutely free from <a href="https://github.com/Dene33/blender_renderActions">github</a>    But feel free to buy it if you'll find it useful! Thank you!</p>
