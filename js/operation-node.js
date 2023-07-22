import {app} from "/scripts/app.js";

app.registerExtension({
    name: "ComfyLiterals.OperationNode",
    nodeCreated(node, app) {
        if (node['comfyClass'] === 'Operation') {
            /**
             * @type {Record<string, INodeInputSlot>}
             */
            const inputCache = {
                "A": node.inputs[1],
                "B": node.inputs[3]
            }

            // Node has 4 inputs(IntA, FloatA, IntB, FloatB)
            // Remove both float inputs, Float B moves to index 2 after Float A is removed
            node.removeInput(1)
            node.removeInput(2)

            // Add a toggle widget to the node
            node.widgets[0].callback = function (v, canvas, node) {
                addInputAtIndex(node, inputCache["A"], 0)
                inputCache["A"] = node.inputs[1]
                node.removeInput(1)
            }
            node.widgets[1].callback = function (v, canvas, node) {
                addInputAtIndex(node, inputCache["B"], 2)
                inputCache["B"] = node.inputs[1]
                node.removeInput(1)
            }

            node.onConfigure = function (nodeInfo) {
                // Correct the cache if the inputs have been changed
                // This is needed for copy/paste to work correctly
                if (nodeInfo.inputs[0].name === "A - Int") {
                    inputCache["A"] = {name: "A - Float", type: "FLOAT", link: null}
                } else if (nodeInfo.inputs[0].name === "A - Float") {
                    inputCache["A"] = {name: "A - Int", type: "INT", link: null}
                }

                if (nodeInfo.inputs[1].name === "B - Int") {
                    inputCache["B"] = {name: "B - Float", type: "FLOAT", link: null}
                } else if (nodeInfo.inputs[1].name === "B - Float") {
                    inputCache["B"] = {name: "B - Int", type: "INT", link: null}
                }
            }
        }
    }
})

/**
 * Adds an input to a node at the given index.
 * @param node {LGraphNode}
 * @param input {INodeInputSlot}
 * @param index {number}
 * @returns {INodeInputSlot}
 */
function addInputAtIndex(node, input, index) {
    if (!node.inputs) {
        node.inputs = [];
    }

    if (index > node.inputs.length) {
        console.warn("LiteGraph: Warning adding port index: " + index + " of node " + node.id + ", it doesnt have so many inputs");
        node.inputs.push(input);
    } else {
        node.inputs.splice(index, 0, input);
    }
    if (node.onInputAdded) {
        node.onInputAdded(input);
    }
    node.setSize(node.computeSize());
    LiteGraph.registerNodeAndSlotType(node, input.type || 0);

    node.setDirtyCanvas(true, true);
    return input;
}
